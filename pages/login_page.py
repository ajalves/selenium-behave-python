from context.driver import driver
from pages.locators import SignInPageLocators
from pages.locators import HomePageLocators

from pages.page import Page
from selenium.webdriver.common.keys import Keys


class LoginPage(Page):
    """Object to represent the login page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_continue(self):
        continue_button = super().get_element(SignInPageLocators.CONTINUE_BUTTON)

    def fill_email(self, email):
        email_field = super().get_element(SignInPageLocators.EMAIL_FIELD)
        continue_button = super().get_element(SignInPageLocators.CONTINUE_BUTTON)
        email_field.send_keys(email)
        continue_button.click()

    def fill_password(self, password):
        password_field = super().get_element(SignInPageLocators.PASSWORD_FIELD)
        signin_button = super().get_element(SignInPageLocators.SIGNIN_BUTTON)
        password_field.send_keys(password)
        signin_button.click()

    def verify_user_logged(self, username):
        text = super().get_element_text(HomePageLocators.LOGIN_BUTTON)
        assert text == "Hola " + username, "User is not logged in or user name is not correct"

    def login(self, email, password, username):
        self.fill_email(email)
        self.fill_password(password)
        self.verify_user_logged(username)


login_page = LoginPage.get_instance()
