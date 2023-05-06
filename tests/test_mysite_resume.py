import pytest
from playwright.sync_api import Page
from pages.james_home import JamesHomePage
from pages.james_resume import JamesResumePage
from playwright.sync_api import Page, expect


@pytest.mark.skip(reason="Skipping this test for now")
def test_load_mysite(page: Page) -> None: # (page: Page) - add page fixture
    james_home_page = JamesHomePage(page)
    james_resume_page = JamesResumePage(page)

    # given the JamesChen home page is displayed
    james_home_page.load()

    # verify menu links is Resume
    james_home_page.resume_link.wait_for() # playwright explicit wait
    
    # when the user click on the Resume link
    james_home_page.resume_link.click()

    # then the Resume page is displayed and the url is 'https://jameszschen.com/resume/'
    expect(james_resume_page.resume_header_text).to_have_text('Resume')
    assert page.url == james_resume_page.resume_url, \
        f"Unexpected link text! Expected: {james_resume_page.resume_url}, Actual: {page.url}"
    #page.screenshot(path='test-finished.png')
   
    page.close()
