from playwright.sync_api import Page

class gmail_InboxPage:


    # constructor like and pass playwright page
    def __init__(self, page: Page) -> None:
        self.page = page

        # locator objects
        self.profile_button = page.locator('img.gb_j.gbii')
        self.frame_profile_menu = page.frame_locator("iframe[name='account']")
        
        # locate iframe child element
        self.profile_menu = self.frame_profile_menu.locator('div.Wdz6e')

    def wait_profile_menu_visible(self) -> None:
        self.page.wait_for_selector(self.profile_menu)

        