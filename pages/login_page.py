from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "login" in self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.ENTER_FORM), "Login form is not presented"

        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(self, email, password):
        # email = str(time.time()) + "@fakemail.org"
        # password = "123456789"
        self.browser.find_element_by_css_selector("#id_registration-email").send_keys(email)
        self.browser.find_element_by_css_selector("#id_registration-password1").send_keys(password)
        self.browser.find_element_by_css_selector("#id_registration-password2").send_keys(password)
        self.browser.find_element_by_css_selector(".register_form .btn-primary").click()



