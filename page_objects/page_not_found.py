from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class PageNotFound(BasePage):
    # locators
    __url = "http://localhost/404"
    __link_to_user_page_locator = "//a[@href='/user']"
    __home_button_locator = (By.XPATH, "//button[@color='accent']")
    __heading_locator = (By.XPATH, "//h1[@color='primary']")
    __sub_heading_locator = (By.TAG_NAME, "p")
    __logo_locator = (By.XPATH, "//img[contains(@src,'xcnt-logo-white.png')]")

    # page text
    __expected_heading_text = "Whoops!"
    __expected_heading_sub_text = "It seems like we couldn't find the page you were looking for"

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def expected_heading_text(self):
        return self.__expected_heading_text

    @property
    def expected_heading_sub_text(self):
        return self.__expected_heading_sub_text

    @property
    def actual_heading_text(self) -> str:
        return super()._get_text(self.__heading_locator)

    @property
    def actual_sub_heading_text(self) -> str:
        return super()._get_text(self.__sub_heading_locator)

    @property
    def is_logo_displayed(self):
        return super()._is_displayed(self.__logo_locator)

    def click_on_xcnt_logo(self):
        return super()._click(self.__logo_locator)

    def click_on_home_button(self):
        return super()._click(self.__home_button_locator)
