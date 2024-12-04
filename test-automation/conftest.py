import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()