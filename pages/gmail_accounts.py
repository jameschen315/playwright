import time
import json
from playwright.sync_api import Page


class gmail_AccountPage:

    # class variable
    with open('data_file.json') as f:
        data = json.load(f)
    
    # Extract username and password from data
    username = data['username']
    password = data['password']
    url = data['gmail_url']
    # url = 'https://gmail.com'
    # username = 'sfsukid2@gmail.com'
    # password = 'Happytester972'


    # constructor like and pass playwright page
    def __init__(self, page: Page) -> None:
        self.page = page

        # locator objects
        self.account_header_text = page.locator('id=headingText')
        self.sign_in_button = page.locator('id=identifierId')
        self.email_input = page.locator("input[type='email']")
        self.password_input = page.locator("input[type='password']")
        self.next_button = page.locator("button[class*='VfPpkd-LgbsSe-OWXEXe-k8QpJ'] span")
        self.not_now_link = page.locator("button[class*='yu6jOd'] span")

    def load_gmail_homepage(self) -> None:
        self.page.goto(self.url)

    
    def wait_account_header_visible(self) -> None:
        self.page.wait_for_selector(self.account_header_text)
    
    def sign_into_gmail(self) -> None:
        self.email_input.click()
        self.email_input.fill(self.username)
        self.next_button.click()
        time.sleep(1)
        self.password_input.click()
        self.password_input.fill(self.password)
        self.next_button.click()
    
    def dismiss_not_now_gds(self) -> None:
        '''
        Dismiss google ads if the 'not now' link is available
        '''
        if self.not_now_link.is_visible():
            self.not_now_link.click()
        else:
            pass