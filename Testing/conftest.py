import pytest
from playwright.sync_api import sync_playwright
from Playwright.Utils import navigateToCategory

@pytest.fixture(scope='class')
def page_setup(request):
    with sync_playwright() as playwright:
        subcategory = request.param
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(), 'Elements', subcategory)
        yield page