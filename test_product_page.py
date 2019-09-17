# Run me with: pytest -s -v --tb=line --language=ru test_product_page.py
from random import shuffle
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

PRODUCT_URL = ''
products = [
    'the-shellcoders-handbook_209/?promo=newYear',
    'coders-at-work_207/?promo=newYear2019',
    'the-city-and-the-stars_95/'
]
shuffle(products)
PRODUCT_URL = 'http://selenium1py.pythonanywhere.com/catalogue/' + products[0]

def test_guest_should_see_add_to_basket_button(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_be_add_to_basket_button()

@pytest.mark.parametrize('promo_code',
                         [
                             0, 1, 2, 3, 4, 5, 6,
                             pytest.param(7, marks=pytest.mark.xfail),
                             8, 9
                         ])
def test_guest_can_add_product_to_basket(browser, promo_code):
    PRODUCT_URL = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_name = product_page.find_product_name()
    product_page.should_see_product_name_identical_to_message(product_name)
    product_price = product_page.find_product_price()
    product_page.should_see_product_price_identical_to_message(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.should_success_message_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_URL)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
