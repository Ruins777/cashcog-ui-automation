import time

from page_objects.default_user_page import DefaultUserPage
from page_objects.page import Page
from page_objects.page_not_found import PageNotFound


class TestPageNotFound:
    def test_invalid_path_url(self, driver):
        """
        Test if user is navigated to 404 page if he tries to access url with invalid route
        :param driver:
        :return:
        """

        # user enters invalid url
        Page.open(driver, "http://localhost/abc")

        page_not_found = PageNotFound(driver)
        assert page_not_found.current_url == "http://localhost/404", "invalid url is navigated to 404 page"

    def test_page_not_found_elements(self, driver):
        """
        Test for elements present on 404 page
        :param driver:
        :return:
        """

        # user enters invalid url
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)
        assert page_not_found.actual_heading_text == page_not_found.expected_heading_text, ("heading text is not as "
                                                                                            "expected")
        assert page_not_found.actual_sub_heading_text == page_not_found.actual_sub_heading_text, ("sub-heading text is "
                                                                                                  "not as expected")
        assert page_not_found.is_logo_displayed, "xcnt logo is not displayed"

    def test_page_not_found_logo_click_navigation(self, driver):
        """
        Test for if user is navigated to 'user details' page if he clicks on xcnt logo
        :param driver:
        :return:
        """

        # user enters invalid url
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)

        # user clicks on xcnt logo
        page_not_found.click_on_xcnt_logo()

        default_user_page = DefaultUserPage(driver)
        assert default_user_page.current_url == default_user_page.expected_url, \
            "Clicking on logo does not navigate to default user page"

    def test_page_not_found_home_button_click_navigation(self, driver):
        """
        Test for if user is navigated to 'user details' page if he clicks on 'HOME' button
        :param driver:
        :return:
        """

        # user enters invalid url
        Page.open(driver, "http://localhost/nmk")
        page_not_found = PageNotFound(driver)

        # user clicks on home button
        page_not_found.click_on_home_button()
        default_user_page = DefaultUserPage(driver)

        assert default_user_page.current_url == default_user_page.expected_url, \
            "Clicking on home button does not navigate to default user page"
