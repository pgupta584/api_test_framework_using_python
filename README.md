# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* Repo link
* https://github.com/pgupta584/api_test_framework_using_python.git
* This is for Report Validation Framework

### After Installing new Package ###

Configure virtual environment in IDE :

    python3 -m venv env

A folder **env** will be created. Activate the virtual environment :

    source env/bin/activate

Install the requirements :

    pip3 install -r requirements.txt

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

# Whenever add new Package / Dependencies
* do  **exit**
* then do **source START** 
* source start has the command to install prerequisite available into requirements.txt

# How to Run
pytest -s -m {markerName} --host={Env} --disable-pytest-warnings

Example:

pytest -s -m "smoke" --host=prod --disable-pytest-warnings

# How to Run with allure report

** Run Locally & Generate Allure Report **
pytest -s -m "smoke" --host=prod --alluredir="allure_dir" --disable-pytest-warnings
allure serve allure_dir

