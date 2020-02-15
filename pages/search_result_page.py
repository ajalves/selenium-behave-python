from context.driver import driver
from pages.locators import SignInPageLocators
from pages.locators import SearchResultPageLocators
from pages.locators import ItemPageLocators

from pages.page import Page


class SearchResultsPage(Page):
    """Object to represent the search result page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = SearchResultsPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def verify_search_results(self):
        assert super().element_exists(SearchResultPageLocators.SEARCH_RESULT) is True, (
            "Expected search result was not found on the search page"
        )

    def click_item(self):
        search_item = super().get_element(SearchResultPageLocators.SEARCH_RESULT)
        search_item.click()
        # Verify Item page is displayed
        assert super().element_exists(ItemPageLocators.ADD_CART_BUTTON) is True


search_results_page = SearchResultsPage.get_instance()
