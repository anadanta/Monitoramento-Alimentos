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
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh 'source venv/bin/activate && pytest'
            }
        }
    }
}
