
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(5)
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(5)
    login_page.should_be_login_page()
    time.sleep(5)


def test_guest_should_see_login_link (browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()



