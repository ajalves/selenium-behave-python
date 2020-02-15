from behave import given, when, then, step
from pages.homepage_amazon import home_page
from pages.search_result_page import search_results_page
from pages.item_page import item_page
from pages.locators import SearchResultPageLocators
from context.config import settings
from context.driver import driver
from pages.login_page import login_page

"""Hooks for interacting with amazon"""


@given(u'I load the website')
def load_website(context):
    driver.navigate(settings.url)


@step(u'I login with email and password')
def login_step(context):
    home_page.click_login()
    login_page.login(settings.email, settings.password, settings.username)


@when(u'I search for "{search_term}"')
def search(context, search_term):
    home_page.search(search_term)
    search_results_page.verify_search_results()


@step('I add item from brand "{brand_name}"')
def add_item_step(context, brand_name):
    search_results_page.click_item()
    item_page.click_add_to_cart()


@then("I should see the item in my cart")
def verify_cart_step(context):
    item_page.click_cart()
    assert search_results_page.element_exists(SearchResultPageLocators.SEARCH_RESULT) is True, "item is not present " \
                                                                                               "in cart. "
