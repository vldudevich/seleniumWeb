from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM)
        email_form.send_keys(email)
        password_form1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM)
        password_form1.send_keys(password)
        password_form2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM2)
        password_form2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.BTN_SUBMIT_REG)
        btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "what it this?" in self.browser.currect_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "No login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "No autorizacion form"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "No register form"
        assert True