import pytest
from playwright.sync_api import Page
from pages.gmail_accounts import gmail_AccountPage
from pages.gmail_inbox import gmail_InboxPage
from playwright.sync_api import Page, expect


# @pytest.mark.skip(reason="Skipping this test for now")
def test_gmail_login(page: Page) -> None:
    '''
    Test sign into gmail and verify the correct gmail is displayed
    '''
    gmail_account_page = gmail_AccountPage(page)
    gmail_inbox_page = gmail_InboxPage(page)

    # sign into gmail account
    gmail_account_page.load_gmail_homepage()
    gmail_account_page.sign_into_gmail()

    # verify user is successfully login to the right account
    gmail_inbox_page.profile_button.click()
    
    # switch to iframe
    gmail_inbox_page.profile_menu.is_visible()
    expect(gmail_inbox_page.profile_menu).to_have_text(gmail_account_page.username)

    page.close()

