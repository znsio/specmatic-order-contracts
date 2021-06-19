#!/usr/bin/env

import json
import os


def read_event_data():
    event_data_file = os.environ['GITHUB_EVENT_PATH']
    with open(event_data_file) as f:
        return json.loads(f.read())


def log_call(fn):
    def log_wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__} -----")
        result = fn(*args, **kwargs)
        print(result)
        return result

    return log_wrapper


@log_call
def get_commit_range(event_data):
    return (event_data['before'], event_data['after'])

@log_call
def get_commit_ids(event_data):
    if 'commits' not in event_data:
        return []

    commits = event_data['commits']
    return [commit['id'] for commit in commits]


def flatten(list_of_items):
    return [item for sublist in list_of_items for item in sublist]


@log_call
def load_meta_data(file_path):
    with open(file_path) as f:
        return json.loads(f.read())["pipelines"]


def line_to_pipeline_data(line):
    organization, project, definitionId = line.split()
    return {"organization": organization, "project": project, "definitionId": int(definitionId)}


@log_call
def get_changed_contracts_in_range(commit_range):
    commit_ids_str = ' '.join(commit_range)
    git_command = f"git diff --name-only {commit_ids_str}"
    stream = os.popen(git_command)
    raw_lines = stream.readlines()
    lines = [line.strip() for line in raw_lines]
    return [path for path in lines if path.endswith(".qontract")]


@log_call
def get_changed_contracts(commit_ids):
    commit_ids_str = ' '.join(commit_ids)
    git_command = f"git show --name-only --format=tformat: {commit_ids_str}"
    stream = os.popen(git_command)
    raw_lines = stream.readlines()
    lines = [line.strip() for line in raw_lines]
    return [path for path in lines if path.endswith(".qontract")]


def to_meta_file_name(path):
    return os.path.splitext(path)[0] + ".json"


def invoke_pipeline(owner, repo, event_type, access_token_name):
    print(f"Invoking pipeline for owner {owner}, repo {repo}, type {event_type}")
    payload = "{\"event_type\":\"" + event_type + "\"}"
    command = f"curl -X POST -H \"Authorization: token ${access_token_name}\" -H 'Accept: application/vnd.github.v3+json' -d '{payload}' https://api.github.com/repos/{owner}/{repo}/dispatches"
    print(command)
    stream = os.popen(command)
    print(stream.read())


@log_call
def invoke_pipelines(pipelines, access_token_name):
    for pipeline in pipelines:
        invoke_pipeline(**dict(pipeline, access_token_name=access_token_name))


@log_call
def get_meta_data_paths(changed_contracts):
    paths = [to_meta_file_name(contract) for contract in changed_contracts]
    return [path for path in paths if os.path.isfile(path)]


@log_call
def get_pipelines(meta_data_file_paths):
    return flatten([load_meta_data(file_path) for file_path in meta_data_file_paths])


ACCESS_TOKEN_NAME = os.environ['ACCESS_TOKEN_NAME']

event_data = read_event_data()
commit_range = get_commit_range(event_data)
changed_contracts = get_changed_contracts_in_range(commit_range)
meta_data_file_paths = get_meta_data_paths(changed_contracts)
pipelines = get_pipelines(meta_data_file_paths)
invoke_pipelines(pipelines, ACCESS_TOKEN_NAME)
