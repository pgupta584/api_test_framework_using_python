from pytest import mark

from config.api_config import ApiUrls
from req_res.request.gorest import GoRest
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


class TestGetUser:
    @mark.getUser
    @mark.user
    def test_get_user_details(self):
        GET_USER_URL = ApiUrls.GET_USER
        print("URL --> ", GET_USER_URL)
        header = CommonUtility.get_custom_header()
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=GET_USER_URL,
                                                               headers=header)
        print(response.json())
        print("API Success")

    @mark.createUser
    def test_create_user(self):
        GET_USER_URL = ApiUrls.GET_USER
        print("URL --> ", GET_USER_URL)
        header = CommonUtility.get_custom_header()
        json_req = GoRest.CREATE_USER
        json_req['email'] = CommonUtility.get_unique_email()
        response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                               request_url=GET_USER_URL,
                                                               headers=header,
                                                               request_json=json_req,
                                                               expected_status_code=201
                                                               )
        print(response.json())
        print("POST API Success")

    @mark.user
    def test_get_user_details_1(self):
        print("User details 1 fired")

