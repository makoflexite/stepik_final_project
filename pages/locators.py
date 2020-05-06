from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_VIEW = (By.CSS_SELECTOR, ".btn-group>a")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    # product = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p")
    BASKET_SUM = (By.CSS_SELECTOR, ".alert-info .alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success  .alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "# content_inner>p>a")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
