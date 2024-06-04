pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
              git 'https://github.com/pgupta584/api_test_framework_using_python.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
              sh 'echo "Setup Python Environment - Already install as Plugin in Jenkins"'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'export PATH=$PATH:/path/to/pytest'
                sh 'pytest -m "getUser"'
            }
        }

        stage('Generate Allure Report') {
            steps {
              sh 'echo "Generate Allure Report"'
            }
        }

        stage('Publish Allure Report') {
            steps {
              sh 'echo "Publish Allure Report"'
            }
        }
    }
}