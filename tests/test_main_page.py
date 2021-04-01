from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_quest_should_see_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.text_basket_is_empty_should_be_present()




