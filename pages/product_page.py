from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_basket(self):
        button_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_link.click()

    def get_name_of_product(self):
        product_name_link = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert "Coders at Work" == product_name_link.text, "error"

    def should_not_be_message_one(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE), \
            "Success message is presented, but should not be"
        assert True

    def should_be_message_two(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE), \
            "Success message is dissapered, but should not be"
        assert True