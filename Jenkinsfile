pipeline {
    agent any

    environment {
        NESTJS_WEBHOOK_URL = 'http://localhost:3000/api/jenkins/webhook'
        REPO_URL = 'https://github.com/your-org/your-repo.git'
        BRANCH_PREFIX = 'fix/jenkins-'
        COMMIT_MESSAGE = 'Auto-fix: Jenkins test failures'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh 'python -m pytest --junitxml=test-results.xml'
                        currentBuild.result = 'SUCCESS'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        echo "Tests failed, notifying NestJS for auto-repair..."
                        notifyNestJS()
                        throw e
                    }
                }
            }
        }

        stage('Archive Results') {
            steps {
                junit 'test-results.xml'
                archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo "Pipeline completed with result: ${currentBuild.result}"
        }
        failure {
            echo "Build failed - NestJS should handle auto-repair"
        }
    }
}

def notifyNestJS() {
    def payload = [
        project: 'python-demo',
        repoUrl: env.REPO_URL,
        branchPrefix: env.BRANCH_PREFIX,
        commitMessage: env.COMMIT_MESSAGE,
        testResults: [
            status: 'FAILED',
            details: 'Python pytest tests failed'
        ]
    ]

    httpRequest(
        url: env.NESTJS_WEBHOOK_URL,
        httpMode: 'POST',
        contentType: 'APPLICATION_JSON',
        requestBody: groovy.json.JsonBuilder(payload).toString(),
        ignoreSslErrors: true
    )
}