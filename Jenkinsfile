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

        stage('Run Pytest') {
            steps {
                dir('/') {
                    python test_python_hello.py
                }
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