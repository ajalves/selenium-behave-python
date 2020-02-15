from context.driver import driver
from pages.locators import SignInPageLocators
from pages.locators import SearchResultPageLocators
from pages.locators import ItemPageLocators

from pages.page import Page


class ItemPage(Page):
    """Object to represent the item selected page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ItemPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def click_cart(self):
        cart_button = super().get_element(ItemPageLocators.CART_COUNT_NUMBER)
        cart_button.click()

    def click_add_to_cart(self):
        add_cart_button = super().get_element(ItemPageLocators.ADD_CART_BUTTON)
        cart_items_before = super().get_element_text(ItemPageLocators.CART_COUNT_NUMBER)
        add_cart_button.click()
        # Verify cart item numbers was incremented
        cart_items_after = super().get_element_text(ItemPageLocators.CART_COUNT_NUMBER)
        assert int(cart_items_after) is int(cart_items_before) + 1, "After clicking add cart button item count was " \
                                                                    "not incremented. "


item_page = ItemPage.get_instance()
