
from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage):
    def add_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


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


