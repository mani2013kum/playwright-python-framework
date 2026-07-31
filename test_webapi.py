
from playwright.sync_api import Playwright, expect

from __pycache__.utils.apiBase import APIUtils


def test_webapi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    api_utils=APIUtils()
    order_id=api_utils.createorder(playwright)

    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("mani2013kum@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Manisha@1996")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button",name="ORDERS").click()

    #order history page->order id is present
    row=page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    page.pause()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
    
    


    