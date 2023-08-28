from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage


class DefaultUserPage(BasePage):
    # locator
    __heading_locator = (By.XPATH, "//h1")
    __create_user_button_locator = (By.XPATH, "//button/span[contains(text(), 'Create User')]")
    # __first_name_column_locator = (By.XPATH, "//table/tbody/tr[{}]/td[contains(@class, 'mat-column-firstName')]")
    __first_name_column_locator = (By.XPATH, "//td[1]")
    __last_name_column_locator = (By.XPATH, "//td[2]")
    __email_column_locator = (By.XPATH, "//td[3]")
    __newsletter_signup_status_locator = (By.XPATH, "//td[4]/mat-icon")
    __delete_user_row_locator = (By.XPATH, "//td/a/mat-icon[contains(text(), 'delete_outline')]")
    __deselected_newsletter_locator_pattern = "//table/tbody/tr[{}]/td[contains(@class, 'mat-column-newsletter')]/mat-icon[contains(text(), 'clear')]"
    __selected_newsletter_locator_pattern = "//table/tbody/tr[{}]/td[contains(@class, 'mat-column-newsletter')]/mat-icon[contains(text(), 'done')]"
    __delete_user_row_locator_pattern = "//tr[{}]/td/a/mat-icon[contains(text(), 'delete_outline')]"
    __all_first_name_columns_locator = (By.XPATH, "//td[contains(@class, 'mat-column-firstName')]")
    __no_records_locator = (By.XPATH, "//mat-card/p")
    __all_user_rows_locator = (By.XPATH, "//table/tbody/tr")

    # url
    __url = "http://localhost/user"

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def _add_row_no_to_locator(self, row_no: int, locator_type: By, locator: str) -> tuple:
        return locator_type, locator.format(str(row_no))

    def get_first_name_from_column(self, row_element: WebElement) -> str:
        return row_element.find_element(*self.__first_name_column_locator).text

    def get_last_name_from_column(self, row_element: WebElement) -> str:
        return row_element.find_element(*self.__last_name_column_locator).text

    def get_email_from_column(self, row_element: WebElement) -> str:
        return row_element.find_element(*self.__email_column_locator).text

    def get_newsletter_status_from_column(self, row_element: WebElement) -> str:
        return row_element.find_element(*self.__newsletter_signup_status_locator).text

    def get_delete_button_from_column(self, row_element: WebElement) -> WebElement:
        return row_element.find_element(*self.__delete_user_row_locator)

    def verify_data_in_all_columns(self, expected_first_name: str,
                                   expected_last_name: str,
                                   expected_email: str,
                                   newsletter_signup: bool) -> bool:
        rows = super()._get_all_rows_in_table(self.__all_user_rows_locator)
        if newsletter_signup:
            expected_newsletter_signup_text = "done"
        else:
            expected_newsletter_signup_text = "clear"

        for row in rows:
            first_name = self.get_first_name_from_column(row)
            last_name = self.get_last_name_from_column(row)
            email = self.get_email_from_column(row)
            newsletter_status_text = self.get_newsletter_status_from_column(row)
            if (first_name == expected_first_name and
                    last_name == expected_last_name and email == expected_email
                    and newsletter_status_text == expected_newsletter_signup_text):
                return True
        else:
            return False

    def delete_all_user_records(self):
        try:
            super()._get_text(self.__no_records_locator)
        except TimeoutException as n:
            while len(super()._get_all_rows_in_table(self.__all_user_rows_locator)) > 1:
                rows = super()._get_all_rows_in_table(self.__all_user_rows_locator)
                row, *tail = rows
                delete_button = self.get_delete_button_from_column(row)
                delete_button.click()
            else:
                delete_button = super()._find(self.__all_user_rows_locator)
                delete_button.click()

    @property
    def no_records_message(self) -> str:
        return super()._get_text(self.__no_records_locator)

    @property
    def expected_url(self) -> str:
        return self.__url

    def click_create_user_button(self):
        super()._click(self.__create_user_button_locator)




