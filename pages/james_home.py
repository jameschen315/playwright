from playwright.sync_api import Page

class JamesHomePage:

    # class variable
    url = 'https://jameszschen.com'

    # constructor like and pass playwright page
    def __init__(self, page: Page) -> None:
        self.page = page
        # locator objects
        self.home_link = page.locator('id=menu-item-22')
        self.about_link = page.locator('id=menu-item-21')
        self.about_skills_link = page.locator('id=menu-item-21')
        self.contact_link = page.locator('id=menu-item-18')
        self.resume_link = page.locator('id=menu-item-1911')

   # print(f'current url is: {actual_url}')

    def load(self) -> None:
        self.page.goto(self.url)

    def wait_homepage_visible(self) -> None:
        self.page.wait_for_selector(self.home_link)
         