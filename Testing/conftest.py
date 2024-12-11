import pytest
from playwright.sync_api import sync_playwright
from Playwright.Utils import navigateToCategory

@pytest.fixture(scope='function')
def page_setup(request):
    with sync_playwright() as playwright:
        category,subcategory = request.param
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(), category, subcategory)
        page.add_style_tag(content="""
                    iframe, [id*='ads'], [class*='ads'], .banner {
                        display: none !important;
                    }
                """)
        yield page
