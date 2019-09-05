# Run me with: pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.login_page import LoginPage

MAIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/'

def test_guest_should_see_login_link(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    main_page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
