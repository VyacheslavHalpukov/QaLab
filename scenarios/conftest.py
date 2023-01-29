from pytest import fixture

from framework.utils.browser_utils import Browser
from scenarios.resources.page_urls import PageUrls


@fixture()
def base_ui() -> None:
    """
    Fixture for base UI actions: start and quit Browser
    """
    browser = Browser()
    browser.get_driver()
    yield
    browser.quit_driver()


@fixture
def ui_with_automation_page(base_ui) -> None:
    """Fixture with automation practice page in tests"""
    Browser.navigate_to(PageUrls.AUTOMATION_PRACTICE_FORM)
    yield
