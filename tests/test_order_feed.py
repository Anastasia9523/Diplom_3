import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.modal_page import ModalPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
@allure.story("Счётчики увеличиваются после заказа")
@allure.title("Создание заказа увеличивает статистику и добавляет заказ в 'В работе'")
def test_order_increase(authorized_user):

    driver = authorized_user
    wait = WebDriverWait(driver, 25)

    main = MainPage(driver)
    modal = ModalPage(driver)
    feed = OrderFeedPage(driver)

    
    with allure.step("Открываем ленту заказов и сохраняем значения счетчиков"):
        modal.close_if_open()
        main.go_to_feed()
        feed.wait_loaded()

        total_before = feed.get_total_done()
        today_before = feed.get_today_done()


    with allure.step("Переходим в конструктор и создаем заказ"):
        modal.close_if_open()
        main.go_to_constructor()
        main.wait_constructor_loaded()

        main.add_bun_to_constructor()
        main.add_filling_to_constructor()

        main.click_order_button()
        modal.wait_order_open()

        order_number = modal.get_order_number()
        modal.close_order_modal()


    with allure.step("Возвращаемся в ленту заказов и проверяем увеличение счётчиков"):
        modal.close_if_open()
        main.go_to_feed()
        feed.wait_loaded()

        wait.until(lambda d: feed.get_total_done() > total_before)
        wait.until(lambda d: feed.get_today_done() > today_before)


    with allure.step("Проверяем, что заказ появился в списке 'В работе'"):

        wait.until(lambda d: order_number in feed.get_orders_in_progress())
