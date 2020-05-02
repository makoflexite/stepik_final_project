from .base_page import BasePage

class ProductPage(BasePage):
    def add_to_busket(self):
        # login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # *says that we gave pair of parameters and this cortege should be unpacked
        # login_link.click()
        pass

    def should_be_login_link(self):
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        pass