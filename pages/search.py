from playwright.sync_api import Page

class DuckDuckGoSearchPage:

    # class variable
    URL = 'https://www.duckduckgo.com'

    # constructor like and pass playwright page
    def __init__(self, page: Page) -> None:
        self.page = page
        # locator objects
        self.search_input = page.locator('id=searchbox_input')
        self.search_button = page.locator('.searchbox_searchButton__F5Bwq.iconButton_button__6x_9C')

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()



