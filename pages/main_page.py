# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        """ Конструктор с ключевым словом super вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage"""
        super(MainPage, self).__init__(*args, **kwargs)