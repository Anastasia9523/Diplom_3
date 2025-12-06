import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.modal_locators import ModalLocators as L


class ModalPage(BasePage):

    @allure.step("Ожидание открытия модалки ингредиента")
    def wait_ingredient_open(self):
        self.wait.until(EC.visibility_of_element_located(L.CONTAINER))
        self.wait.until(EC.visibility_of_element_located(L.INGREDIENT_TITLE))

    @allure.step("Ожидание открытия модалки заказа")
    def wait_order_open(self):
        self.wait.until(EC.visibility_of_element_located(L.ORDER_NUMBER))

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.wait.until(
            EC.visibility_of_element_located(L.ORDER_NUMBER)
        ).text.strip()

    @allure.step("Закрыть модалку")
    def close(self):

    # Пробуем кликнуть overlay или крестик
        for locator in (L.OVERLAY, L.CLOSE_BTN):
            try:
                btn = self.wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].click();", btn)
                break
            except:
                pass

    # После любого метода закрытия — обязательно ждём исчезновения overlay и контейнера!
        self.wait.until(EC.invisibility_of_element_located(L.CONTAINER))

    # overlay иногда исчезает позже контейнера → ждём его тоже
        try:
            self.wait.until(EC.invisibility_of_element_located(L.OVERLAY))
        except:
            pass

    @allure.step("Закрыть заказ (alias для тестов)")
    def close_order_modal(self):
        self.close()

    @allure.step("Проверка: открыта ли модалка")
    def is_open(self):
        try:
            WebDriverWait(self.driver, 0.5).until(
                EC.visibility_of_element_located(L.CONTAINER)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Закрыть модалку, если открыта")
    def close_if_open(self):
        if self.is_open():
            self.close()
