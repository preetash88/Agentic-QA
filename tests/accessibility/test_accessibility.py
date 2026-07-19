from playwright.sync_api import Page


def test_homepage_accessibility(page: Page):
    page.goto("https://automationexercise.com")

    assert page.locator("body").is_visible()