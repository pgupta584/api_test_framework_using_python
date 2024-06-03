import logging

import allure
from pytest import mark

from config.api_config import ApiUrls
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils

logger = logging.getLogger()
logger.setLevel(logging.ERROR)


@allure.suite("User Service API")
class TestGetUser:
    @mark.getUser
    @mark.user
    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    @allure.title("Test to verify get user by valid data")
    def test_get_user_details_valid(self):
        GET_USER_URL = ApiUrls.GET_USER
        print("URL --> ", GET_USER_URL)
        logger.info(f"URL is --> {GET_USER_URL}")
        header = CommonUtility.get_custom_header()
        logger.info(f"Header is --> {header}")
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=GET_USER_URL,
                                                               headers=header)
        logger.info(f"Response is --> {response.json()}")
        logger.info(f"Status code is --> {response.status_code}")
        assert response.status_code == 200, "API Success"
        # json_schema.match(response.json(), "req_res/response/get_user.json")
        print(response.json())
        print("API Success")

    @mark.getUser
    @mark.user
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.title("Test to verify get user by Invalid Auth Token")
    def test_get_user_details_invalid_auth(self):
        GET_USER_URL = ApiUrls.GET_USER
        print("URL --> ", GET_USER_URL)
        logger.info(f"URL is --> {GET_USER_URL}")
        header = CommonUtility.get_custom_header()
        header['Authorization'] = "wrong"
        logger.info(f"Header is --> {header}")
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=GET_USER_URL,
                                                               headers=header)
        if response.status_code != 401:
            logger.error(f"Response is --> {response.json()}")
            logger.error(f"Actual Status code is --> {response.status_code} but expected is 401, that's why it's failed")
        print(response.json())
        assert response.status_code == 401, "Status code is wrong"
        print("API Success")
