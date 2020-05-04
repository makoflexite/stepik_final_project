from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver

class ProductPage(BasePage):
    def add_to_busket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON) # *says that we gave pair of parameters and this cortege should be unpacked
        add_to_basket.click()

    def should_be_product_added(self):
        self.should_be_successfull_info()
        self.should_be_same_product_name_in_basket()
        self.should_be_same_price()

    def should_be_successfull_info(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No seccessfull message about adding"

    def should_be_same_product_name_in_basket(self):
        print("Product name is ", self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "---", " Name in success message is ", \
              self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text)
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, \
            "Other product name is written in message about adding"
        # assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME).text in self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE).text, \
        #     "Other product name is written in message about adding"

    def should_be_same_price(self):
        print("Sum in basket = ", self.browser.find_element(*ProductPageLocators.BASKET_SUM).text, "---",
              "Price of the product = ", self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Price of product and basket sum are not same"



