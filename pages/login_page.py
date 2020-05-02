from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert ('/login/' in self.browser.current_url), f"URL is not from login page, it is {self.browser.current_url}"

    def should_be_login_form(self):
        # checking that login form locator exists
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # checking that register form locator exists
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"