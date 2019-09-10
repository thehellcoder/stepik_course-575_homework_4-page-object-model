# Run me with: pytest -s -v --tb=line --language=ru test_product_page.py
from pages.product_page import ProductPage

PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/'
               'the-shellcoders-handbook_209/?promo=newYear')

def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_see_correct_success_messages()
