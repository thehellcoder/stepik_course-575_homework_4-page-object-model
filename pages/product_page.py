from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()
    
    def should_see_correct_success_messages(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert name.text == messages[0].text, \
            'Product name was changed while adding to empty basket'
        assert price.text == messages[2].text, \
            'Product price was changed while adding to empty basket'
