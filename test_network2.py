import time
from playwright.sync_api import Page
def intercept_request(route):
        route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a648eb585b8849b490c4f3b")

def test_network1(page:Page):
        page.goto("https://rahulshettyacademy.com/client")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?*",intercept_request )
            
        page.get_by_placeholder("email@example.com").fill("mani2013kum@gmail.com")
        page.get_by_placeholder("enter your passsword").fill("Manisha@1996")
        page.get_by_role("button",name="Login").click()
        page.get_by_role("button",name="ORDERS").click()
        page.get_by_role("button",name="View").first.click()
        time.sleep(5)
        message=page.locator(".blink_me").text_content()
        print(message)


