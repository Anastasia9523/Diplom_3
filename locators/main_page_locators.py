from selenium.webdriver.common.by import By

class MainPageLocators:

    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BTN = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    INGREDIENT_CARD = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient')]")

    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "div.counter_counter__ZNLkj")

    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//div[contains(@class,'BurgerConstructor')]")


