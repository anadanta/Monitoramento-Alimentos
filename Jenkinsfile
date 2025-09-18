pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                git branch: 'main', credentialsId: 'github-token', url: 'https://github.com/anadanta/Monitoramento-Alimentos.git'
            }
        }
        stage('Setup and Install') {
            steps {
                echo 'Setting up and installing dependencies...'
                sh '''#!/bin/bash -l
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''#!/bin/bash -l
                    source venv/bin/activate
                    pytest
                '''
            }
        }
    }
}
