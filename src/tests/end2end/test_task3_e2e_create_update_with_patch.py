# Create Booking -> Patch


import pytest
import allure
import requests

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *


class TestE2E_Patch(object):

    @allure.title("Create New Booking -> Update with Patch request")
    @allure.description("Verify that user is able to create a fresh booking & generate a token, "
                        "then update this booking partially")
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)
        booking_id = get_booking_id
        token = create_token
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        print(patch_url)

        response = patch_requests(
            url=patch_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_patch_booking(),
            auth=None,
            in_json=False
        )
        # Verification here & more
        verify_http_status_code(response_data=response, expected_data=200)

        verify_response_key(response.json()["firstname"], "James")
        print("Booking ", booking_id, "updated successfully!. Firstname updated to ", response.json()["firstname"])

