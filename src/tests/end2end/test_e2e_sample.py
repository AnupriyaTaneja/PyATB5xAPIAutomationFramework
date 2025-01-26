import allure
import pytest

class TestE2E(object):

    @allure.title("E2E - Create Booking -> Update -> Delete(Verify)")
    @allure.description("Verify that booking id is created, and we are able to update and delete it also | Full CRUD")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1",name="E2ETC1")
    def test_update_booking_with_id_token(self):
        pass

    @allure.title("Test CRUD operation -> DELETE")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self):
        pass