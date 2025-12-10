from selenium.webdriver.common.by import By

class ModalLocators:

    CONTAINER = (By.CSS_SELECTOR, "div[class*='Modal_modal__container']")
    OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
    CONTENT = (By.CSS_SELECTOR, "div[class*='Modal_modal__contentBox']")
    CLOSE_BTN = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    
    INGREDIENT_TITLE = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')]")
