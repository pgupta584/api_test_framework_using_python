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
                sh 'pip install pytest'
                sh 'pip install request'
            }
        }
        stage('Run Tests') {
            steps {
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