from playwright.sync_api import Page

class JamesResumePage:

    # constructor like and pass playwright page
    def __init__(self, page: Page) -> None:
        self.page = page
        # locator objects
        self.resume_url = 'https://jameszschen.com/resume/'
        self.resume_header_text = page.locator('.elementor-heading-title.elementor-size-default')
         