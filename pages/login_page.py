from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        substring = 'login'
        assert substring in current_url, f"substring '{substring}' is not part of string '{current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*BasePageLocators.EMAIL_ADDRESS)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*BasePageLocators.PASSWORD)
        password_field.send_keys(password)
        repeat_password_field = self.browser.find_element(*BasePageLocators.REPEAT_PASSWORD)
        repeat_password_field.send_keys(password)
        register_field = self.browser.find_element(*BasePageLocators.REGISTER)
        register_field.click()
