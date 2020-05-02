# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # *says that we gave pair of parameters and this cortege should be unpacked
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"