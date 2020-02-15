from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""

    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class HomePageLocators:
    """Class for amazon home page selectors"""
    LOGIN_BUTTON = Locator(By.CLASS_NAME, "nav-line-1")
    SEARCH_BAR = Locator(By.ID, "twotabsearchtextbox")
    SEARCH_RESULT = Locator(By.XPATH, "//a[@href='{}']")


class SignInPageLocators:
    """Class for amazon SignIn page selectors"""
    EMAIL_FIELD = Locator(By.NAME, "email")
    PASSWORD_FIELD = Locator(By.NAME, "password")
    CONTINUE_BUTTON = Locator(By.ID, "continue")
    SIGNIN_BUTTON = Locator(By.ID, "signInSubmit")


class SearchResultPageLocators:
    """Class for amazon search result page selectors"""
    SEARCH_RESULT = Locator(By.CSS_SELECTOR, "img[alt *= 'AUELEK']")


class ItemPageLocators:
    ADD_CART_BUTTON = Locator(By.ID, "add-to-cart-button")
    CART_COUNT_NUMBER = Locator(By.ID, "nav-cart-count")
