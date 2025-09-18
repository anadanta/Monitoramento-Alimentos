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
                    cd backend
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Migrate Database') {
            steps {
                echo 'Migrating database...'
                sh '''#!/bin/bash -l
                    cd backend
                    source venv/bin/activate
                    python3 manage.py makemigrations --settings=sistema_monitoramento.settings_test
                    python3 manage.py migrate --settings=sistema_monitoramento.settings_test
                '''
            }
        }
        stage('Start Server') {
            steps {
                echo 'Starting Django server...'
                sh '''#!/bin/bash -l
                    cd backend
                    source venv/bin/activate
                    python3 manage.py runserver 0.0.0.0:8000 &
                    sleep 5
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''#!/bin/bash -l
                    cd backend
                    source venv/bin/activate
                    pytest
                    pkill -f 'python3 manage.py runserver'
                '''
            }
        }
    }
}
