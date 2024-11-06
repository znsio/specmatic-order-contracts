pipeline {
    agent any

     environment {
        // Define environment variables
        SPECMATIC_ORG_ID = "66fe6c555e232d36a28fef94"  // Stored in Jenkins credentials
        WORKSPACE = pwd()  // Get Jenkins workspace path
    }
    
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
                    // Get Jenkins job information
                    def jobName = env.JOB_NAME
                    def buildNumber = env.BUILD_NUMBER
                    def branchName = env.BRANCH_NAME ?: 'main'  // Fallback to 'main' if not available
                    
                    // Get repository information from Git
                    def repoUrl = sh(script: 'git config --get remote.origin.url', returnStdout: true).trim()
                    def repoName = repoUrl.tokenize('/').last().replace('.git', '')
                    
                    // Run Specmatic Insights reporter
                    docker.image('znsio/specmatic-insights-github-build-reporter:latest').inside("-v ${WORKSPACE}:/workspace") {
                        sh """
                            /app/specmatic-insights-reporter \
                            --specmatic-insights-host https://insights.specmatic.in \
                            --specmatic-reports-dir /workspace/build/reports/specmatic \
                            --org-id ${SPECMATIC_ORG_ID} \
                            --branch-ref refs/heads/${branchName} \
                            --branch-name ${branchName} \
                            --build-definition-id "${jobName}" \
                            --build-id ${buildNumber} \
                            --repo-name ${repoName} \
                            --repo-id ${jobName.hashCode()} \
                            --repo-url ${repoUrl}
                        """
                    }
                }
            }
            // steps {
            //     script {
            //         def githubToken = env.GH_REPOSITORY_TOKEN
            //         def orgId = '66fe6c555e232d36a28fef94'
            //         def branchRef = env.GIT_BRANCH
            //         def branchName = env.GIT_BRANCH
            //         def buildId = env.BUILD_ID
            //         def repoName = env.GIT_REPO_NAME
            //         def repoId = env.GIT_REPO_ID
            //         def repoUrl = env.GIT_URL

            //         def jsonPayload = """
            //         {
            //             "github-token": "${githubToken}",
            //             "org-id": "${orgId}",
            //             "branch-ref": "${branchRef}",
            //             "branch-name": "${branchName}",
            //             "build-id": "${buildId}",
            //             "repo-name": "${repoName}",
            //             "repo-id": "${repoId}",
            //             "repo-url": "${repoUrl}"
            //         }
            //         """

            //         sh """
            //         curl -X POST -H "Content-Type: application/json" \
            //         -d '${jsonPayload}' \
            //         https://insights.specmatic.io/report
            //         """
            //     }
            // }
        }
    }
}
