from playwright.sync_api import Page
fakeorderpayLoadResponse={"data":[],"message":"No Orders"}
def intercept_response(route):
        route.fulfill(json=fakeorderpayLoadResponse)
        
def test_network1(page:Page):
        page.goto("https://rahulshettyacademy.com/client")
        page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
            
        page.get_by_placeholder("email@example.com").fill("mani2013kum@gmail.com")
        page.get_by_placeholder("enter your passsword").fill("Manisha@1996")
        page.get_by_role("button",name="Login").click()
        page.get_by_role("button",name="ORDERS").click()
        order_text=page.locator(".mt-4").text_content()
        print(order_text)
        