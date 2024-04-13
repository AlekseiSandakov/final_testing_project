from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_is_disappeared_success_message(self):
        cart = self.browser.find_element(*BasePageLocators.EMPTY_CART)
        substring = 'Your basket is empty'
        text_cart = cart.text
        print(text_cart)
        assert substring in text_cart, f"substring '{substring}' is not part of string '{text_cart}'"
