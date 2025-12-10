from selenium.webdriver.common.by import By

class OrderFeedLocators:
    TOTAL_DONE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    TODAY_DONE = (By.XPATH,"//p[text()='Выполнено за сегодня:']/following-sibling::p")

    ORDERS_IN_PROGRESS = (By.XPATH, "(//div[contains(@class,'OrderFeed_orderStatusBox')]//ul)[1]/li")

    DONE_ORDERS = (By.XPATH, "(//div[contains(@class,'OrderFeed_orderStatusBox')]//ul)[2]/li")

    HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
