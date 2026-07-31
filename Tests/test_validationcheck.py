
from playwright.sync_api import Page, expect
def test_validationcheck(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect (page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect (page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    #Handling alert
    page.on("dialog",lambda dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()
    
#Framehandling
    # Locate the iframe
    frame = page.frame_locator("#courses-iframe")
    # Click Learning Paths
    frame.get_by_role("link", name="Learning Paths").click()
    
