import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators as L
from data.urls import BASE_URL


class LoginPage(BasePage):

    URL = BASE_URL + "/login"

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Войти в аккаунт")
    def login(self, email, password):

        email_input = self.find(L.EMAIL)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.find(L.PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(L.BUTTON)

