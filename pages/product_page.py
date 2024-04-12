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
        text_product_name = message_product_name.text
        text = f'{text_product_name} in the basket'
        print(text)
        assert text_product_name in text, f"substring '{text_product_name}' is not part of string '{text}'"

    def should_be_cart_cost(self):
        car_cost = self.browser.find_element(*AddToCartLocators.CART_COST)
        cost_product = self.browser.find_element(*AddToCartLocators.COST_PRODUCT)
        cost = car_cost.text
        price = cost_product.text
        print(f'cart cost {cost}, the price of the product {price}')
        assert cost == price, "The cost of the cart is not equal to the price of the product"
