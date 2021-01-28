
from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):

    def is_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.GOODS_ITEMS), "корзина не пуста"

    def text_cart_is_empty(self):
        assert self.browser.find_element(*CartPageLocators.TEXT_GOODS_LICT),\
            "нет текста о пустой корзине"



