
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    ENTER_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSEGE_ADD_TO_CARD_SHOW = (By.CSS_SELECTOR, ".alert-success strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MESSEGE_PRIСE = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")




