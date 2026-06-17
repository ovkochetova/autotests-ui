from playwright.sync_api import expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')
        self.login_button = Button(page, 'login-page-login-button', 'Login button')

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self, email: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

    def click_login_button(self):
        self.login_button.click()
        


