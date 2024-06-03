import json

import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="prod")


def update_env(config):
    with open("/Users/payzapp-automation/PycharmProjects/api_test/config/endpoints.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.truncate(0)
        jsonFile.seek(0)
        data['environment']['env'] = config.getoption("--host").lower()
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()


@pytest.hookimpl()
def pytest_configure(config):
    update_env(config)
