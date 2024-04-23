from allure_commons._allure import step
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


def test_search():
    with step("Search Pulp Fiction"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Pulp Fiction")
    with step("Check what we found"):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Pulp Fiction"))
    with step("Step into topic"):
        results.first.click()
