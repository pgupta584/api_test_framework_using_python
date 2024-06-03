pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repository.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest --junitxml=test-results.xml
                    deactivate
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'
            }
        }
    }
}