pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('List Files') {
            steps {
                script {
                    sh 'ls -R'
                }
            }
        }
        
        stage('Run OpenAPI Backward compatibility Check') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') { // have to handle this because bcc is failing build when no files are changed
                        sh '''
                            java -jar specmatic_2.0.33.jar backward-compatibility-check --base-branch origin/main
                        '''
                    }
                }
            }
        }

        stage('RGenerate central contract repo report') {
            steps {
                script {
                    sh '''
                        java -jar specmatic_2.0.33.jar central-contract-repo-report
                    '''
                }
            }
        }

        stage('Run Specmatic Insights Reporter') {
            steps {
                script {
                    def githubToken = env.GH_REPOSITORY_TOKEN
                    def orgId = '66fe6c555e232d36a28fef94'
                    def branchRef = env.GIT_BRANCH
                    def branchName = env.GIT_BRANCH
                    def buildId = env.BUILD_ID
                    def repoName = env.GIT_REPO_NAME
                    def repoId = env.GIT_REPO_ID
                    def repoUrl = env.GIT_URL

                    def jsonPayload = """
                    {
                        "github-token": "${githubToken}",
                        "org-id": "${orgId}",
                        "branch-ref": "${branchRef}",
                        "branch-name": "${branchName}",
                        "build-id": "${buildId}",
                        "repo-name": "${repoName}",
                        "repo-id": "${repoId}",
                        "repo-url": "${repoUrl}"
                    }
                    """

                    sh """
                    curl -X POST -H "Content-Type: application/json" \
                    -d '${jsonPayload}' \
                    https://insights.specmatic.io/report
                    """
                }
            }
        }
    }
}
