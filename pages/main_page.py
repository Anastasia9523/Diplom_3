import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from data.urls import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.wait.until(EC.element_to_be_clickable(L.CONSTRUCTOR_BTN)).click()

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.wait_modal_closed()
        btn = self.wait.until(EC.element_to_be_clickable(L.FEED_BTN))
        self.js_click(btn) 

    @allure.step("Ожидание загрузки конструктора")
    def wait_constructor_loaded(self):
        self.wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_DROP_ZONE))

    @allure.step("Получить список ингредиентов")
    def get_all_ingredients(self):
        return self.find_all(L.INGREDIENT_CARD)

    @allure.step("Клик по ингредиенту №{index}")
    def click_ingredient(self, index):
        self.get_all_ingredients()[index].click()

    @allure.step("Получить счётчик ингредиента №{index}")
    def get_ingredient_counter(self, index):
        ingredient = self.get_all_ingredients()[index]
        blocks = ingredient.find_elements(*L.INGREDIENT_COUNTER)
        if not blocks:
            return 0
        try:
            return int(blocks[0].find_element(By.TAG_NAME, "p").text.strip())
        except:
            return 0

    @allure.step("Перетаскивание ингредиента №{index}")
    def drag_ingredient_to_constructor_by_index(self, index):

        source = self.get_all_ingredients()[index]
        target = self.find(L.CONSTRUCTOR_DROP_ZONE)

        self.wait.until(EC.visibility_of(source))
        self.wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_DROP_ZONE))

        self.scroll_into_view(source)
        self.scroll_into_view(target)

        self.drag_and_drop(source, target)

        self.wait.until(lambda d: self.get_ingredient_counter(index) > 0)

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
                continue
