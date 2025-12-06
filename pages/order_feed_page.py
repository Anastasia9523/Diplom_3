import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as L


class OrderFeedPage(BasePage):

    @allure.step("Ожидание загрузки страницы 'Лента заказов'")
    def wait_loaded(self):
        self.wait.until(EC.visibility_of_element_located(L.HEADER))

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_total_done(self):
        return int(self.find(L.TOTAL_DONE).text)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_today_done(self):
        return int(self.find(L.TODAY_DONE).text)

    @allure.step("Получить список заказов в блоке 'В работе'")
    def get_orders_in_progress(self):
        items = self.find_all(L.ORDERS_IN_PROGRESS)
        return [i.text.strip() for i in items if i.text.strip()]
    
    def get_done_orders(self):
        items = self.find_all(L.DONE_ORDERS)
        return [i.text.strip() for i in items if i.text.strip()]