import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.modal_page import ModalPage
from locators.modal_locators import ModalLocators


@allure.feature("Конструктор")
class TestConstructorFlow:

    @allure.story("Переход в Конструктор")
    @allure.title("Клик по кнопке «Конструктор» открывает нужный раздел")
    def test_constructor_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Конструктор»"):
            main.go_to_constructor()

        with allure.step("Проверяем, что открылись ингредиенты"):
            assert "Булки" in driver.page_source

    @allure.story("Переход в Ленту заказов")
    @allure.title("Клик по кнопке «Лента заказов» работает корректно")
    def test_feed_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Лента заказов»"):
            main.go_to_feed()

        with allure.step("Проверяем URL"):
            assert "/feed" in driver.current_url

    @allure.story("Модалка ингредиента")
    @allure.title("Открытие модалки ингредиента по клику")
    def test_ingredient_modal_open(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Кликаем по первому ингредиенту"):
            main.click_ingredient(0)

        with allure.step("Ожидаем появления модалки"):
            modal.wait_ingredient_open()

        with allure.step("Проверяем, что модалка действительно открыта"):
            assert modal.is_open(), "Модалка ингредиента не открылась"

    @allure.story("Модалка ингредиента")
    @allure.title("Закрытие модалки ингредиента по крестику")
    def test_ingredient_modal_close(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Открываем модалку ингредиента"):
            main.click_ingredient(0)
            modal.wait_ingredient_open()

        with allure.step("Закрываем модалку"):
            modal.close()

        with allure.step("Проверяем, что модалка исчезла"):
            assert not modal.is_open(), "Модалка ингредиента не закрылась"

    @allure.story("Счётчики ингредиентов")
    @allure.title("Счётчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        wait = WebDriverWait(driver, 10)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Получаем список ингредиентов"):
            ingredients = main.get_all_ingredients()

        with allure.step("Находим первый небулочный ингредиент"):
            index = None
            for i, item in enumerate(ingredients):
                img = item.find_element("tag name", "img")
                alt = (img.get_attribute("alt") or "").lower()
                if "булка" not in alt:
                    index = i
                    break
            assert index is not None, "Нет небулочных ингредиентов"

        with allure.step(f"Читаем счётчик ингредиента №{index}"):
            counter_before = main.get_ingredient_counter(index)

        with allure.step("Добавляем ингредиент в конструктор (drag&drop)"):
            main.drag_ingredient_to_constructor_by_index(index)

        with allure.step("Ожидаем, что счётчик увеличится"):
            import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.modal_page import ModalPage
from locators.modal_locators import ModalLocators


@allure.feature("Конструктор")
class TestConstructorFlow:

    @allure.story("Переход в Конструктор")
    @allure.title("Клик по кнопке «Конструктор» открывает нужный раздел")
    def test_constructor_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Конструктор»"):
            main.go_to_constructor()

        with allure.step("Проверяем, что открылись ингредиенты"):
            assert "Булки" in driver.page_source

    @allure.story("Переход в Ленту заказов")
    @allure.title("Клик по кнопке «Лента заказов» работает корректно")
    def test_feed_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Лента заказов»"):
            main.go_to_feed()

        with allure.step("Проверяем URL"):
            assert "/feed" in driver.current_url

    @allure.story("Модалка ингредиента")
    @allure.title("Открытие модалки ингредиента по клику")
    def test_ingredient_modal_open(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Кликаем по первому ингредиенту"):
            main.click_ingredient(0)

        with allure.step("Ожидаем появления модалки"):
            modal.wait_ingredient_open()

        with allure.step("Проверяем, что модалка действительно открыта"):
            assert modal.is_open(), "Модалка ингредиента не открылась"

    @allure.story("Модалка ингредиента")
    @allure.title("Закрытие модалки ингредиента по крестику")
    def test_ingredient_modal_close(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Открываем модалку ингредиента"):
            main.click_ingredient(0)
            modal.wait_ingredient_open()

        with allure.step("Закрываем модалку"):
            modal.close()

        with allure.step("Проверяем, что модалка исчезла"):
            assert not modal.is_open(), "Модалка ингредиента не закрылась"

    @allure.story("Счётчики ингредиентов")
    @allure.title("Счётчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        wait = WebDriverWait(driver, 10)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Получаем список ингредиентов"):
            ingredients = main.get_all_ingredients()

        with allure.step("Находим первый небулочный ингредиент"):
            index = None
            for i, item in enumerate(ingredients):
                img = item.find_element("tag name", "img")
                alt = (img.get_attribute("alt") or "").lower()
                if "булка" not in alt:
                    index = i
                    break
            assert index is not None, "Нет небулочных ингредиентов"

        with allure.step(f"Читаем счётчик ингредиента №{index}"):
            counter_before = main.get_ingredient_counter(index)

        with allure.step("Добавляем ингредиент в конструктор (drag&drop)"):
            main.drag_ingredient_to_constructor_by_index(index)

        with allure.step("Ожидаем, что счётчик увеличится"):
            import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.modal_page import ModalPage
from locators.modal_locators import ModalLocators


@allure.feature("Конструктор")
class TestConstructorFlow:

    @allure.story("Переход в Конструктор")
    @allure.title("Клик по кнопке «Конструктор» открывает нужный раздел")
    def test_constructor_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Конструктор»"):
            main.go_to_constructor()

        with allure.step("Проверяем, что открылись ингредиенты"):
            assert "Булки" in driver.page_source

    @allure.story("Переход в Ленту заказов")
    @allure.title("Клик по кнопке «Лента заказов» работает корректно")
    def test_feed_button(self, driver):
        main = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main.open_page()

        with allure.step("Переходим в раздел «Лента заказов»"):
            main.go_to_feed()

        with allure.step("Проверяем URL"):
            assert "/feed" in driver.current_url

    @allure.story("Модалка ингредиента")
    @allure.title("Открытие модалки ингредиента по клику")
    def test_ingredient_modal_open(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Кликаем по первому ингредиенту"):
            main.click_ingredient(0)

        with allure.step("Ожидаем появления модалки"):
            modal.wait_ingredient_open()

        with allure.step("Проверяем, что модалка действительно открыта"):
            assert modal.is_open(), "Модалка ингредиента не открылась"

    @allure.story("Модалка ингредиента")
    @allure.title("Закрытие модалки ингредиента по крестику")
    def test_ingredient_modal_close(self, driver):
        main = MainPage(driver)
        modal = ModalPage(driver)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Открываем модалку ингредиента"):
            main.click_ingredient(0)
            modal.wait_ingredient_open()

        with allure.step("Закрываем модалку"):
            modal.close()

        with allure.step("Проверяем, что модалка исчезла"):
            assert not modal.is_open(), "Модалка ингредиента не закрылась"

    @allure.story("Счётчики ингредиентов")
    @allure.title("Счётчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        wait = WebDriverWait(driver, 10)

        with allure.step("Открываем страницу конструктора"):
            main.open_page()
            main.go_to_constructor()
            main.wait_constructor_loaded()

        with allure.step("Получаем список ингредиентов"):
            ingredients = main.get_all_ingredients()

        with allure.step("Находим первый небулочный ингредиент"):
            index = None
            for i, item in enumerate(ingredients):
                img = item.find_element("tag name", "img")
                alt = (img.get_attribute("alt") or "").lower()
                if "булка" not in alt:
                    index = i
                    break
            assert index is not None, "Нет небулочных ингредиентов"

        with allure.step(f"Читаем счётчик ингредиента №{index}"):
            counter_before = main.get_ingredient_counter(index)

        with allure.step("Добавляем ингредиент в конструктор (drag&drop)"):
            main.drag_ingredient_to_constructor_by_index(index)

        with allure.step("Ожидаем, что счётчик увеличится"):
            assert main.get_ingredient_counter(index) > counter_before, \
                "Счётчик ингредиента не увеличился после добавления"
