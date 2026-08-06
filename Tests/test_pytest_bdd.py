import pytest
from pytest_bdd import given, scenarios, then, when
from pytest_bdd import parsers
from pageobjects.Login import LoginPage
from utils.apiBaseFramework import APIUtils
from pageobjects.orderDetailpage import orderDetailpage
scenarios(r"C:\Users\Manisha\Downloads\saucedemo\features\OrderTransaction.feature")
@pytest.fixture
def shared_data():
    return{}
@given(parsers.parse('place order with {username} and {password}'))
def place_item_order(playwright,username,password,shared_data):
    user_credentials={}
    user_credentials["userEmail"]= username
    user_credentials["userPassword"]=password
    api_utils=APIUtils()
    order_id=api_utils.createorder(playwright,user_credentials)
    shared_data['order_id']= order_id

@given('user is on  landing page')
def user_on_landingpage(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page']=loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username,password,shared_data):
    loginPage=shared_data['login_page']
    dashboardpage = loginPage.login(username, password)
    shared_data['dashboard_page']=dashboardpage
@when('Navigate to orders page')
def navigate_order(shared_data):
    dashboardpage = shared_data['dashboard_page']
    ordersHistorypage = dashboardpage.selectOrdersNavLink()
    shared_data['ordersHistorypage'] = ordersHistorypage
    

@when('select the order')
def navigate_order(shared_data): 
    ordersHistorypage=shared_data['ordersHistorypage']
    order_id=shared_data['order_id']
    orderdetailspage=ordersHistorypage.selectorder(order_id)
    shared_data['orderdetail_page']=orderdetailspage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
     orderdetailpage=shared_data['orderdetail_page']
     orderdetailpage.verifyorderdetails()
    


