from pages.locators import HomePageLocators
from pages.locators import SignInPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class HomePage(Page):
    """Object to represent the amazon search splash page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_login(self):
        login_button = super().get_element(HomePageLocators.LOGIN_BUTTON)
        login_button.click()
        # Confirm next page is loaded
        super().element_exists(SignInPageLocators.EMAIL_FIELD)

    def search(self, search_term):
        search_bar = super().get_element(HomePageLocators.SEARCH_BAR)
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)


home_page = HomePage.get_instance()
