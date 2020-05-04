from .pages.main_page import MainPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    page.should_be_product_added()


