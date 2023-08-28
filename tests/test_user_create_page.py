import time

from page_objects.default_user_page import DefaultUserPage
from page_objects.user_create_page import UserCreatePage


class TestUserCreatePage:
    def test_blank_input_fields(self, driver):
        user_create_page = UserCreatePage(driver)

        # opens user create page
        user_create_page.open()

        # click on first name field
        user_create_page.click_on_first_name()

        # click on last name field so that error pops up in first name
        user_create_page.click_on_last_name()

        # check if error message for blank first name is displayed
        assert user_create_page.first_name_field_error_message == "First name is required.", \
            "Error message for blank first name is not displayed"

        # click on email field so that error pops up in last name
        user_create_page.click_on_email()

        # check for last name blank error message
        assert user_create_page.last_name_field_error_message == "Last name is required.", \
            "Error message for blank last name is not displayed"

        # click on first name field so that error pops up in email
        user_create_page.click_on_first_name()
        assert user_create_page.email_blank_field_error_message == "Email is required.", \
            "Error message for blank email is not displayed"

    def test_blank_fields_error_message_on_submit(self, driver):
        """
        This test case checks if error message is displayed on all blank input fields
        if submit button is pressed
        :param driver:
        """
        user_create_page = UserCreatePage(driver)

        # opens user create page
        user_create_page.open()

        # click on submit
        user_create_page.click_on_submit()

        # check all error messages on input fields together
        assert user_create_page.first_name_field_error_message == "First name is required.", \
            "Error message for blank first name is not displayed"

        assert user_create_page.last_name_field_error_message == "Last name is required.", \
            "Error message for blank last name is not displayed"

        assert user_create_page.email_blank_field_error_message == "Email is required.", \
            "Error message for blank email is not displayed"

    # invalid email
    def test_for_invalid_email(self, driver):
        user_create_page = UserCreatePage(driver)

        # opens user create page
        user_create_page.open()

        # enter invalid email
        user_create_page.enter_email("e@")
        user_create_page.click_on_submit()

        assert user_create_page.email_invalid_field_error_message == "Please enter a valid email.", \
            "Error message for invalid email is not displayed"

    # def test_for_new_user_creation_with_checkbox_selected(self, driver):
    #     # delete all existing user records
    #     default_user_page = DefaultUserPage(driver)
    #     default_user_page.open()
    #     default_user_page.delete_all_user_records()
    #     # default_user_page.click_create_user_button()
    #     # user_create_page = UserCreatePage(driver)
    #     #
    #     # # enter user details
    #     # user_create_page.enter_user_details("in", "xs", "inxs@group.com", True)
    #     # user_create_page.click_on_submit()
    #     #
    #     # default_user_page = DefaultUserPage(driver)
    #     # assert default_user_page.verify_data_in_all_columns("in", "xs", "inxs@group.com", True)

    def test_duplicate_email_error(self, driver):
        user_create_page = UserCreatePage(driver)

        # opens user create page
        user_create_page.open()
        user_create_page.enter_user_details("h", "h", "h@h.com")
        user_create_page.click_on_submit()

        # create default user page instance
        default_user_page = DefaultUserPage(driver)
        default_user_page.click_create_user_button()
        user_create_page.enter_user_details("h", "h", "h@h.com")
        user_create_page.click_on_submit()
        assert user_create_page.is_email_exists_snackbar_displayed

