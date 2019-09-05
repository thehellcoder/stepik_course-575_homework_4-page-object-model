# Run me with: pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage

MAIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/'

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()
