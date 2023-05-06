import pytest
from playwright.sync_api import Page
from pages.james_home import JamesHomePage
from playwright.sync_api import Page, expect
from urllib.parse import urlparse


@pytest.mark.skip(reason="Skipping this test for now")
def test_mysite_load(page: Page) -> None: # (page: Page) - add page fixture
    james_home_page = JamesHomePage(page)

    # given the JamesChen home page is displayed
    james_home_page.load()
    # when
    # then
    # and
    # and
    # go to jameszschen.com
    
    # return only the domain url
    current_url = page.url
    actual_url = urlparse(current_url).netloc
    expected_url = urlparse(james_home_page.url).netloc

    # verify the page loads is JamesChen.com
    assert expected_url == actual_url, \
        "Unexpected URL! Expected: {}, Actual: {}".format(
        expected_url, actual_url)
 
    # if actualUrl == URL:
    #  print('URL verification successful!')
    # else:
    #  print('URL verification failed. Expected URL: {URL},'
    #        ' Actual URL: {actualUrl}')

    # verify menu links is Resume
    james_home_page.home_link.is_visible()
    # actual_resume_text = james_home_page.resume_link.text_content()
    # expected_resume_text = 'Resume'
    # assert expected_resume_text == actual_resume_text, \
    #     "Unexpected link text! Expected: {}, Actual: {}".format(
    #     expected_resume_text, actual_resume_text)
    expect(james_home_page.resume_link).to_contain_text('Resume')
    

    page.close()
