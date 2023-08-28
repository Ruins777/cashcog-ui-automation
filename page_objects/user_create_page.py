from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class UserCreatePage(BasePage):
    # heading locators
    __heading_locator = (By.TAG_NAME, "h1")

    # first name locator
    __first_name_input_field_locator = (By.XPATH, '//input[@formcontrolname="firstName"]')
    __first_name_input_field_label_locator = (By.XPATH, "(//label/mat-label)[1]")
    __first_name_blank_input_field_error_locator = (By.XPATH, "//mat-error[contains(text(),'First name is required')]")

    # last name locator
    __last_name_input_field_locator = (By.XPATH, "//input[@formcontrolname='lastName']")
    __last_name_input_field_label_locator = (By.XPATH, "(//label/mat-label)[2]")
    __last_name_blank_input_field_error_locator = (By.XPATH, "//mat-error[contains(text(),'Last name is required')]")

    # email locator
    __email_input_field_locator = (By.XPATH, "//input[@formcontrolname='email']")
    __email_input_field_label_locator = (By.XPATH, "(//label/mat-label)[3]")
    __email_blank_input_field_error_locator = (By.XPATH, "//mat-error[contains(text(),'Email is required')]")
    __email_invalid_input_field_error_locator = (By.XPATH, "//mat-error[contains(text(),'Please enter a valid email.')]")
    __email_duplicate_error_locator = (By.XPATH, "//simple-snack-bar")

    # submit button locator
    __submit_button_locator = (By.XPATH, "//button[@type='submit']")

    # create user locator
    __create_user_button = (By.XPATH, "//button[@type='submit']")

    # checkbox button locator
    __checkbox_locator = (By.XPATH, "//mat-checkbox[contains(@class, 'mat-checkbox')]")

    # url
    __url = "http://localhost/user/create"

    # text

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_on_first_name(self):
        super()._clicking_inside_element(self.__first_name_input_field_label_locator)

    def click_on_last_name(self):
        super()._clicking_inside_element(self.__last_name_input_field_label_locator)

    def click_on_email(self):
        super()._clicking_inside_element(self.__email_input_field_locator)

    def click_on_submit(self):
        super()._click(self.__submit_button_locator)

    @property
    def first_name_field_error_message(self) -> str:
        return super()._get_text(self.__first_name_blank_input_field_error_locator)

    @property
    def last_name_field_error_message(self) -> str:
        return super()._get_text(self.__last_name_blank_input_field_error_locator)

    @property
    def email_blank_field_error_message(self) -> str:
        return super()._get_text(self.__email_blank_input_field_error_locator)

    @property
    def email_invalid_field_error_message(self) -> str:
        return super()._get_text(self.__email_invalid_input_field_error_locator)

    @property
    def is_email_exists_snackbar_displayed(self) -> bool:
        return super()._is_displayed(self.__email_duplicate_error_locator)

    def click_on_checkbox(self):
        super()._clicking_inside_element(self.__checkbox_locator)

    def enter_first_name(self, first_name: str):
        super()._enter_text(self.__first_name_input_field_locator, first_name)

    def enter_last_name(self, last_name: str):
        super()._enter_text(self.__last_name_input_field_locator, last_name)

    def enter_email(self, email: str):
        super()._enter_text(self.__email_input_field_locator, email)

    def enter_user_details(self, first_name: str, last_name: str, email: str, signup_checkbox: bool = False):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        if signup_checkbox:
            self.click_on_checkbox()


