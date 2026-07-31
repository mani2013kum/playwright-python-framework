
from playwright.sync_api import Page, expect
def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("visual_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect (page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()

    