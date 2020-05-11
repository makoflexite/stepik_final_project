from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # checking for correct url
        assert ('/login/' in self.browser.current_url), f"URL is not from login page, it is {self.browser.current_url}"

    def should_be_login_form(self):
        # checking that login form locator exists
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # checking that register form locator exists
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        # link = "http://selenium1py.pythonanywhere.com/"
        # page = LoginPage(self.browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # page.open()  # открываем страницу
        # page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        email_form = self.browser.find_element(*RegistrationPageLocators.EMAIL)
        email_form.send_keys(email)
        password1_form = self.browser.find_element(*RegistrationPageLocators.PASSWORD1)
        password1_form.send_keys(password)
        password2_form = self.browser.find_element(*RegistrationPageLocators.PASSWORD2)
        password2_form.send_keys(password)
        button = self.browser.find_element(*RegistrationPageLocators.REG_BUTTON)
        button.click()

