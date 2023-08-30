import time

from page_objects.default_user_page import DefaultUserPage
from page_objects.user_create_page import UserCreatePage


class TestDefaultUserPage:
    def test_table_data_against_input_entered(self, driver):
        """
        This test checks if the records entered on 'create user' page are reflected
        on 'user details' page
        :param driver:
        :return:
        """
        # user deletes all existing user records
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()
        default_user_page.delete_all_user_records()

        # user opens 'CREATE USER' button
        default_user_page.click_create_user_button()
        user_create_page = UserCreatePage(driver)

        # user enters details
        user_create_page.enter_user_details("h", "h", "h@h.com")

        # user clicks on submit
        user_create_page.click_on_submit()

        # check if user is navigated to 'user details' page
        time.sleep(2)
        default_user_page = DefaultUserPage(driver)
        assert default_user_page.current_url == "http://localhost/user",\
            "clicking on 'SUBMIT' button does not navigate to 'user details' page"

        assert default_user_page.verify_data_in_all_columns("h",
                                                            "h",
                                                            "h@h.com",
                                                            False)

    def test_navigation_from_user_create_button_click(self, driver):
        """
        THis test case checks if user is navigated to 'user create' page after clicking on
        'CREATE USER' button
        :param driver:
        :return:
        """
        # user opens 'user details' page
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()

        # user clicks on create user button
        default_user_page.click_create_user_button()

        # user is navigated to 'create user' page
        # wait for dom to load
        time.sleep(2)
        user_create_page = UserCreatePage(driver)
        assert user_create_page.current_url == "http://localhost/user/create", \
            "clicking on 'CREATE USER' does not navigate to create user page"

    def test_for_no_user_records_present(self, driver):
        """
        THis test check when there are no user records, 'No data received!' message is displayed
        :param driver:
        :return:
        """

        # user opens 'user details' page
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()

        # user deletes all existing records, if any
        default_user_page.delete_all_user_records()

        assert default_user_page.no_records_message == "No data received!", "message mismatch for no user records"
