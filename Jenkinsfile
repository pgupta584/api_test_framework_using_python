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
                    pytest -s -m "smoke" --host=prod --alluredir="allure_dir" --disable-pytest-warnings
                    deactivate
                '''
            }
        }
        stage('Publish Allure Results') {
            steps {
                allure serve allure_dir
            }
        }
    }
}