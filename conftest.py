import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.modal_page import ModalPage
from data.user import EMAIL, PASSWORD


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.delete_all_cookies()

    yield driver

    driver.quit()


@pytest.fixture
def authorized_user(driver):

    login = LoginPage(driver)
    modal = ModalPage(driver)

    login.open()

        # закроем overlay, если вдруг остался от прошлого теста
    modal.close_if_open()

    login.login(EMAIL, PASSWORD)

    return driver