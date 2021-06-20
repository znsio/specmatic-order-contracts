#!/bin/sh

curl -X POST -H "Authorization: token $SECRET" -H 'Accept: application/vnd.github.v3+json' -d '{"event_type":"run_action"}' https://api.github.com/repos/znsio/specmatic-order-api/dispatches
curl -X POST -H "Authorization: token $SECRET" -H 'Accept: application/vnd.github.v3+json' -d '{"event_type":"run_action"}' https://api.github.com/repos/znsio/specmatic-order-ui/dispatches
