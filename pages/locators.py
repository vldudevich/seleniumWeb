from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_FORM2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_SUBMIT_REG = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "#content_inner")