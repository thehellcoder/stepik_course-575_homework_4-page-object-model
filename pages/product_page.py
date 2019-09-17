from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BSKT_BTN), \
            'Add to basket button is not presented'
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES), \
            'Success message is presented, but should not be'
    
    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES), \
            'Success message was not disappear'
    
    def click_add_to_basket_button(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BSKT_BTN)
        btn.click()
    
    def should_see_product_name_identical_to_message(self, product_name):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert product_name == messages[0].text, \
            'Product name was changed while adding to empty basket'
    
    def should_see_product_price_identical_to_message(self, product_price):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        assert product_price == messages[2].text, \
            'Product price was changed while adding to empty basket'
    
    def find_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text
    
    def find_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text
