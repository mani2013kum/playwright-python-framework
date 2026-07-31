from playwright.sync_api import Page

def test_openchildwindow(page: Page):
    page.goto("https://demoqa.com")
    with page.expect_popup() as new_page_info:
        page.locator(".banner-image").click()
    child_page = new_page_info.value
    text = child_page.locator(".enroll__heading").text_content()
    print(text)  #Selenium Certification Training | Enroll Now | Study Online
    word=text.split("Certification")
    word1=word[1].strip().split(" ")[0]
    assert word1=="Training"

