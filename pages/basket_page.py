from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "No products in busket, but should be"

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products are in busket, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Success be message about empty busket, but it is not"


    def should_not_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is presented, but should not be"
