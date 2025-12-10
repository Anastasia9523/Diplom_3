import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step("Поиск элемента: {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов: {locator}")
    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Скролл к элементу")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    @allure.step("Перемещение элемента drag&drop")
    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def wait_modal_closed(self):
        from locators.modal_locators import ModalLocators as ML
        try:
            self.short_wait().until(EC.invisibility_of_element_located(ML.CONTAINER))
        except:
            pass
        try:
            self.short_wait().until(EC.invisibility_of_element_located(ML.OVERLAY))
        except:
            pass

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def short_wait(self, timeout=0.5):
        return WebDriverWait(self.driver, timeout)