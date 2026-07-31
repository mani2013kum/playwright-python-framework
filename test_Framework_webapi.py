
import json
from typing import Self

from playwright.sync_api import Playwright, expect
import pytest

from pageobjects.Dashboard import Dashboardpage
from pageobjects.Login import LoginPage
from utils.apiBase import APIUtils


 #json file->util->access into test
with open('Data/credential.json') as f:
     test_data =json.load(f)
     print(test_data)
     user_credential_list=test_data['user_credentials']
@pytest.mark.parametrize('user_credential',user_credential_list)
def test_webapi(playwright:Playwright,user_credential):
    useremail=user_credential["userEmail"]
    userpassword=user_credential["userPassword"]
    
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
   
    #create order->order id
    api_utils=APIUtils()
    order_id=api_utils.createorder(playwright,user_credential)

    
    loginPage = LoginPage(page)
    loginPage.navigate()
    dashboardpage = loginPage.login(useremail, userpassword)
    ordersHistorypage=dashboardpage.selectOrdersNavLink()
    orderdetailspage=ordersHistorypage.selectorder(order_id)
    orderdetailspage.verifyorderdetails()
    
    #order history page->order id is present

    context.close()
    
    


    