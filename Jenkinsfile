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
        stage('Setup Environment') {
            steps {
                echo 'Setting up virtual environment...'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
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
