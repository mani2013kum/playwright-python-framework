import re
import time

from playwright.sync_api import Page, expect
def test_cart(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("visual_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    #Sauce Labs Backpack,Sauce Labs Bike Light-->verify 2 itmes showing in cart
    Backpack=page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    Backpack.locator("#add-to-cart-sauce-labs-backpack").click()
    BikeLight=page.locator(".inventory_item").filter(has_text="Sauce Labs Bike Light")
    BikeLight.locator("#add-to-cart-sauce-labs-bike-light").click()
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".cart_item_label")).to_have_count(2)


    
    
