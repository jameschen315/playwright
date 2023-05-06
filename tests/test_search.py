import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import Page, expect

ANIMALS = [
    'panda',
    'python',
    'parrot',
    'peacock',
    'lion',
    'tiger',
    'whale'
]
# def test_basic_duckduckgo_search(page: Page) -> None:
#     search_page = DuckDuckGoSearchPage(page)
#     result_page = DuckDuckGoResultPage(page)

# Using Fixture
@pytest.mark.parametrize('phrase', ANIMALS)
def test_basic_duckduckgo_search(
        phrase: str,
        page: Page,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    # or page.fill(search_box_input, 'panda') (not recommend since require the element to wait))
    search_page.search(phrase)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase)

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase)

    # And the search result title contains the phrase
    expect(page).to_have_title(f'{phrase} at DuckDuckGo')
