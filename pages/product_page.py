from .base_page import BasePage
from .locators import AddToCartLocators


class ProductPage(BasePage):
    def should_be_add_to_cart(self):
        add_to_cart = self.browser.find_element(*AddToCartLocators.ADD_TO_CART)
        add_to_cart.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*AddToCartLocators.ADD_TO_CART), "Add to cart is not presented"

    def should_be_product_name(self):
        message_product_name = self.browser.find_element(*AddToCartLocators.MESSAGE_PRODUCT_NAME)
        product_name = self.browser.find_element(*AddToCartLocators.PRODUCT_NAME)
        text_message_product_name = message_product_name.text
        text_product_name = product_name.text
        text = f'{text_message_product_name} in the basket'
        print(text)
        assert text_message_product_name == text_product_name, f"substring '{text_product_name}', \
            is not part of string '{text}'"

    def should_be_cart_cost(self):
        car_cost = self.browser.find_element(*AddToCartLocators.CART_COST)
        cost_product = self.browser.find_element(*AddToCartLocators.COST_PRODUCT)
        cost = car_cost.text
        price = cost_product.text
        print(f'cart cost {cost}, the price of the product {price}')
        assert cost == price, "The cost of the cart is not equal to the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddToCartLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*AddToCartLocators.MESSAGE_PRODUCT_NAME), \
            "The success message did not disappear, but should"
