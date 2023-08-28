from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    @classmethod
    def open(cls, driver: WebDriver, url: str):
        driver.get(url)
