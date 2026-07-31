from playwright.sync_api import Playwright
orderPayload= {"orders": [{"country": "India", "productOrderedId": "6960ea76c941646b7a8b3dd5"}]}
class APIUtils:
    def get_token(self,playwright:Playwright,user_credential):
        user_email=user_credential['userEmail']
        user_password=user_credential['userPassword']
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        print(response.json())
        responsebody=response.json()
        return responsebody["token"]

    def createorder(self,playwright:Playwright,user_credential):
       token=self.get_token(playwright,user_credential)
       api_request_context= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
       response=api_request_context.post ("/api/ecom/order/create-order",data= orderPayload,headers={"Authorization":token,"Content-Type":
                                                                                           "application/json"})
       print(response.json())
       response_body=response.json()
       order_id= response_body["orders"][0]
       return order_id
    




           













































        

    
    