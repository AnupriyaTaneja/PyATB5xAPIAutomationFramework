# Update deleted booking

import pytest
import allure
import requests

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *


class TestE2E_All(object):

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        print("Token: ", create_token)
        print("Booking id: ", get_booking_id)
        booking_id = get_booking_id
        d_token = create_token
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

    @allure.title("Update Deleted Booking")
    @allure.description("Verify that user is unable to update an already deleted booking")
    def test_update_deleted_booking(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        book_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=book_id)
        print(put_url)

        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        assert book_id == self.test_delete_booking_id(book_id,token), "Booking doesnt exist"
        #verify_http_status_code(response_data=response, expected_data=200)
        # verify_response_key(response.json()["firstname"], "Amit")
        # verify_response_key(response.json()["lastname"], "Brown")
        # print("Booking ", book_id, "updated successfully!. Firstname updated to ", response.json()["firstname"])
