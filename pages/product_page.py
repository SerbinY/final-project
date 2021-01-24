
from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def add_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        button.click()




    def message_add_to_card_show(self):
        assert self.browser.find_elements(*ProductPageLocators.MESSEGE_ADD_TO_CARD_SHOW),\
            "нет сообщения о успешном добавлении в корзину"
    def name_of_product(self):
        assert self.browser.find_elements(*ProductPageLocators.MESSEGE_ADD_TO_CARD_SHOW)[0].text\
               == self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text,\
            "имя продукта не совпадает с добавленным"

    def message_about_prise(self):
        assert self.browser.find_element(*ProductPageLocators.MESSEGE_PRIСE),\
            "нет сообщения с ценой товара"

    def price_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.MESSEGE_PRIСE).text \
               == self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text,\
            "цена не соответствует"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSEGE_ADD_TO_CARD_SHOW), \
            "Success message is presented, but should not be"


    def shod_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSEGE_ADD_TO_CARD_SHOW), \
            "еллемент не исчез, а должен был"




