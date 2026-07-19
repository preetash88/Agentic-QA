from playwright.sync_api import Page, expect


def test_login_page_loads(page: Page):
    page.goto("https://automationexercise.com/login")

    expect(page.get_by_text("Login to your account")).to_be_visible()

    assert page.locator("text=Login to your account").is_visible()


def test_signup_page_visible(page: Page):
    page.goto("https://automationexercise.com/login")

    assert page.locator("text=New User Signup!").is_visible()