from pages.product_page import ProductPage
import pytest


product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):

    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):

    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.message_should_be_disappeared_after_adding_product_to_basket()
