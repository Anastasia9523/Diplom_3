from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.NAME, "name")
    PASSWORD = (By.NAME, "Пароль")
    BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
