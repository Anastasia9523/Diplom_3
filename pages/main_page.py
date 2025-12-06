import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators.modal_locators import ModalLocators
from pages.base_page import BasePage
from pages.modal_page import ModalPage
from locators.main_page_locators import MainPageLocators as L
from data.urls import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        modal = ModalPage(self.driver)
        modal.close_if_open()

        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(ModalLocators.CONTAINER))

        self.click(L.CONSTRUCTOR_BTN)

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        modal = ModalPage(self.driver)
        modal.close_if_open()

        WebDriverWait(self.driver, 3).until(EC.invisibility_of_element_located(ModalLocators.CONTAINER))

        self.click(L.FEED_BTN)

    @allure.step("Ожидание загрузки конструктора")
    def wait_constructor_loaded(self):
        self.find(L.CONSTRUCTOR_DROP_ZONE)

    @allure.step("Получить список ингредиентов")
    def get_all_ingredients(self):
        return self.find_all(L.INGREDIENT_CARD)

    @allure.step("Клик по ингредиенту №{index}")
    def click_ingredient(self, index):
        items = self.get_all_ingredients()
        items[index].click()

    @allure.step("Получить счётчик ингредиента №{index}")
    def get_ingredient_counter(self, index):
        items = self.get_all_ingredients()
        ingredient = items[index]

        blocks = ingredient.find_elements(*L.INGREDIENT_COUNTER)
        if not blocks:
            return 0

        try:
            p = blocks[0].find_element(By.TAG_NAME, "p")
            return int(p.text.strip())
        except:
            return 0

    @allure.step("Перетаскивание ингредиента №{index}")
    def drag_ingredient_to_constructor_by_index(self, index):

        ingredients = self.get_all_ingredients()
        source = ingredients[index]

        target = self.find(L.CONSTRUCTOR_DROP_ZONE)

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)

        actions = ActionChains(self.driver)

        actions.move_to_element(source).pause(0.2)
        actions.click_and_hold(source).pause(0.3)
        actions.move_to_element(target).pause(0.3)
        actions.move_by_offset(0, 40).pause(0.3) 
        actions.release().perform()
   
    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click(L.ORDER_BUTTON)

    @allure.step("Добавить булки в заказ")
    def add_bun_to_constructor(self):
        self.drag_ingredient_to_constructor_by_index(0)
        self.drag_ingredient_to_constructor_by_index(1)

    @allure.step("Добавить начинку")
    def add_filling_to_constructor(self):
        ingredients = self.get_all_ingredients()
        for i in range(2, len(ingredients)):
            try:
                self.drag_ingredient_to_constructor_by_index(i)
                return
            except:
                pass