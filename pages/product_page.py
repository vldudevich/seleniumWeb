from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        button_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is shown after adding product to basket"

    def message_should_be_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Message isn't dissapeared after adding product to basket"