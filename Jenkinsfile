pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Clonando o repositório..."
            }
        }

        stage('Install Python Dependencies') {
            steps {
                script {
                    echo "Instalando dependências Python do requirements.txt..."
                    sh 'pip install --user -r requirements.txt'
                }
            }
        }

        stage('Run Pytest Tests') {
            steps {
                script {
                    echo "Executando testes com pytest..."
                    sh 'pytest'
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline Python feito com sucesso"
        }
        failure {
            echo "Pipeline Python falhou"
        }
    }
}
