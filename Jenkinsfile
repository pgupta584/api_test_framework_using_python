pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
              sh 'echo "Code Checkout from GIT to Jenkins Machine"'
            }
        }

        stage('Setup Python Environment') {
            steps {
              sh 'echo "Setup Python Environment"'
            }
        }

        stage('Run Pytest') {
            steps {
              sh 'echo "Running Tests"'
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