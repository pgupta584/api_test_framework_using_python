import allure
from pytest import mark

from config.api_config import ApiUrls
from req_res.request.gorest import GoRest
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


@allure.suite("User1 Service API")
class TestGetUser1:

    @mark.createUser
    @mark.smoke
    @mark.user
    def test_create_user1(self):
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
