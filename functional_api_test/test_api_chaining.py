from config.api_config import ApiUrls
from req_res.request.gorest import GoRest
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


def test_api_chaining():
    # url = FunctionalParam.get_base_end_point()
    # print("url", url)
    GET_USER_URL = ApiUrls.GET_USER
    print("GET_USER_URL", GET_USER_URL)

    header = CommonUtility.get_custom_header()
    print("headers", header)
    # print("Testing unique email")
    email = CommonUtility.get_unique_email()
    print(email)
    # print("Getting JSON Request")
    json_req = GoRest.CREATE_USER
    json_req['email'] = email
    print(json_req)
    response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                           request_url=GET_USER_URL,
                                                           headers=header,
                                                           request_json=json_req,
                                                           expected_status_code=201)
    print(response.json())
    print("API Call success")
    user_id = response.json()['id']
    print("User Id is --> ", user_id)

    # Getting User Details
    GET_USER_ID_URL = ApiUrls.get_user_by_id(user_id)
    print("GET_USER_ID_URL", GET_USER_ID_URL)
    print("Testing Headers")
    response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                           request_url=GET_USER_ID_URL,
                                                           headers=header)
    print(response.json())
    response_id = response.json()['id']
    print("Assertion starts")
    assert user_id == response_id, "User is not matched"

test_api_chaining()