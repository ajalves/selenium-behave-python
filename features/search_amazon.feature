Feature: Search Amazon
    This feature searches amazon for an item , verifies that specific item is returned with success, and adds it to the cart
    Scenario: Search
        Given I load the website
        And   I login with email and password
        When I search for "aspirador de coche"
        And I add item from brand "AUELEK"
        Then I should see the item in my cart
