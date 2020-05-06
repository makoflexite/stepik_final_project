from .base_page import BasePage
from .locators import ProductPageLocators
# from selenium import webdriver

class ProductPage(BasePage):
    def add_to_busket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON) # *says that we gave pair of parameters and this cortege should be unpacked
        add_to_basket.click()

    def should_be_product_added(self):
        self.should_be_successfull_info()
        self.should_be_same_product_name_in_basket(self.get_product_name(*ProductPageLocators.PRODUCT_NAME))
        self.should_be_same_price(self.get_product_price(*ProductPageLocators.PRODUCT_PRICE))

    def should_be_successfull_info(self):
        """checking for message about succeed adding"""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No seccessfull message about adding"

    def should_be_same_product_name_in_basket(self, name):
        """checks if product name = name in success message"""
        print("Product name is ", name, "---", " Name in success message is ", self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        assert name == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Other product name is written in message about adding"

    def should_be_same_price(self, price):
        """checks if proce of product = sum in basket"""
        print("Sum in basket = ", self.browser.find_element(*ProductPageLocators.BASKET_SUM).text, "---", "Price of the product = ", price)
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == price, "Price of product and basket sum are not same"
        pass


