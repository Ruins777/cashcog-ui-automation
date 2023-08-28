import pytest

from page_objects.default_user_page import DefaultUserPage


class TestDefaultUserPage:
    def test_table_data_against_input_entered(self, driver):
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()
        assert default_user_page.verify_data_in_all_columns("h",
                                                            "h",
                                                            "h@h.com",
                                                            False)

    def test_table_data_against_invalid_data(self, driver):
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()
        assert not default_user_page.verify_data_in_all_columns("a",
                                                                "h",
                                                                "h@h.com",
                                                                False)

    @pytest.mark.delete
    def test_delete_all_rows_user_table(self, driver):
        default_user_page = DefaultUserPage(driver)
        default_user_page.open()
        default_user_page.delete_all_user_records()
        assert default_user_page.no_records_message == "No data received!", "message mismatch for no user records"
