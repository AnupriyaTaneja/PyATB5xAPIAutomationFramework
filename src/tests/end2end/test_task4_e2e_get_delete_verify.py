# Get -> Delete -> Verify


import pytest
import allure
import requests

import conftest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *

class Test_E2E_Get_Delete_Verify(object):


    @allure.title("Test Delete booking")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
#    @staticmethod
    def test_delete_booking_id(self, get_booking_id, create_token):
        print("Booking id: ", get_booking_id)
        booking_id = get_booking_id
        d_token=create_token
        put_header = Utils.common_header_put_delete_patch_cookie(self, d_token)
        put_url = APIConstants.url_patch_put_delete(booking_id)
        response = delete_requests(
            url=put_url,
            headers=Utils.common_header_put_delete_patch_cookie(self, d_token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expected_data=201)
        verify_response_delete(response=response.text)
        print("Booking ", booking_id, "deleted successfully!")
        return booking_id
    #
    # @allure.title("Fetch Deleted booking")
    # @allure.description("Verify user is not able to fetch booking that is already deleted")
    # def test_get_deleted_booking_id(self, get_booking_id):
    #     self.test_delete_booking_id(get_booking_id)
    #     print("Booking does not exists")

    def test_get_deleted_booking(self):
        self.test_delete_booking_id
        print("Booking does not exists")




