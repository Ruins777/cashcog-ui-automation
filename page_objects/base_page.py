from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
        A base class which will contain variables and methods that are common across webpages

        Attributes
        ----------
        _driver : WebDriver
            holds reference to driver of a browser for a particular session

        Methods
        -------
        _find(locator: tuple)
            takes an element locator in tuple form e.g (By.ID, "some_id")

        _enter_text(locator: tuple, text: str, duration: int = 10)
            enter text in an input element

        _click(self, locator: tuple, duration: int = 10):
            click on an element

        _wait_until_element_is_visible(self, locator: tuple, duration: int = 10)
            implementation of explicit wait. default duration is 10 secs

    """

    def __init__(self, driver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        """ locates an element based on tuple specified.
            The tuple consists of 2 items viz, type of locator and the path/id/class

        Parameters
        ----------
        locator : tuple
            The tuple consists of 2 items viz, type of locator and the path/id/class

        Returns
        -------
        WebElement
            the element located based on locator
        """
        return self._driver.find_element(*locator)

    def _enter_text(self, locator: tuple, text: str, duration: int = 10):
        self._wait_until_element_is_visible(locator, duration)
        self._driver.find_element(*locator).send_keys(text)

    def _click(self, locator: tuple, duration: int = 10):
        self._wait_until_element_is_visible(locator, duration)
        self._driver.find_element(*locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, duration: int = 10):
        wait = WebDriverWait(self._driver, duration)
        wait.until(ec.visibility_of_element_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            self._wait_until_element_is_visible(locator, 10)
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, duration: int = 10):
        self._wait_until_element_is_visible(locator, duration)
        return self._find(locator).text.strip()

    def _clicking_inside_element(self, locator: tuple):
        clickable = self._find(locator)
        ActionChains(self._driver) \
            .click(clickable) \
            .perform()

    def _get_no_of_rows_in_table(self, locator: tuple, duration: int = 10) -> int:
        self._wait_until_element_is_visible(locator, duration)
        return len(self._driver.find_elements(*locator))

    def _get_all_rows_in_table(self, locator: tuple, duration: int = 10) -> list:
        self._wait_until_element_is_visible(locator, duration)
        return self._driver.find_elements(*locator)

