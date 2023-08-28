import time

from page_objects.default_user_page import DefaultUserPage
from page_objects.page import Page
from page_objects.page_not_found import PageNotFound


class TestPageNotFound:
    def test_invalid_path_url(self, driver):
        Page.open(driver, "http://localhost/abc")
        page_not_found = PageNotFound(driver)
        assert page_not_found.current_url == "http://localhost/404", "invalid url is navigated to 404 page"

    def test_page_not_found_elements(self, driver):
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)
        assert page_not_found.actual_heading_text == page_not_found.expected_heading_text, ("heading text is not as "
                                                                                            "expected")
        assert page_not_found.actual_sub_heading_text == page_not_found.actual_sub_heading_text, ("sub-heading text is "
                                                                                                  "not as expected")
        assert page_not_found.is_logo_displayed, "xcnt logo is not displayed"

    def test_page_not_found_logo_click_navigation(self, driver):
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)
        page_not_found.click_on_xcnt_logo()
        default_user_page = DefaultUserPage(driver)
        assert default_user_page.current_url == default_user_page.expected_url, \
            "Clicking on logo does not navigate to default user page"

    def test_page_not_found_home_button_click_navigation(self, driver):
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)
        page_not_found.click_on_home_button()
        default_user_page = DefaultUserPage(driver)
        assert default_user_page.current_url == default_user_page.expected_url, \
            "Clicking on home button does not navigate to default user page"
