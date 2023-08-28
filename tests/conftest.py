from selenium import webdriver
import pytest


# @pytest.fixture(params=["chrome", "edge"])
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"{browser} browser started")
    # open browser
    if browser == "chrome":
        new_driver = webdriver.Chrome()
    elif browser == "firefox":
        new_driver = webdriver.Firefox()
    elif browser == "edge":
        new_driver = webdriver.Edge()
    else:
        raise TypeError(f"Invalid browser {browser} option")
    # new_driver.implicitly_wait(10)
    new_driver.maximize_window()
    yield new_driver
    print(f"{browser} to be closed")
    new_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="enter browser name: chrome / firefox / edge)"
    )
