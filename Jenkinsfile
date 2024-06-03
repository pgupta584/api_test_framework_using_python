pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        ALLURE_RESULTS = 'allure_dir'
        ALLURE_REPORT = 'allure-report'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/pgupta584/api_test_framework_using_python.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    # Create virtual environment
                    python -m venv ${VENV_DIR}

                    # Activate virtual environment
                    source ${VENV_DIR}/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt

                    # Install pytest and allure-pytest
                    pip install pytest allure-pytest
                """
            }
        }

        stage('Run Pytest') {
            steps {
                sh """
                    # Activate virtual environment
                    source ${VENV_DIR}/bin/activate

                    # Run pytest with allure results
                    pytest -s -m "smoke" --host=prod --disable-pytest-warnings --alluredir=${ALLURE_RESULTS}
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh """
                    # Generate Allure report
                    allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}