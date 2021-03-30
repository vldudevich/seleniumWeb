from pages.product_page import ProductPage
import time
import pytest

def test_guest_can_add_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     page = ProductPage(browser, link)
     page.open()
     page.click_basket()
     time.sleep(2)
     page.solve_quiz_and_get_code()
     time.sleep(2)
     page.get_name_of_product()
     page.should_not_be_message_one()
     page.should_be_message_two()


@pytest.mark.xfail(reason="fix_link")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),\
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.click_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    page.get_name_of_product()
