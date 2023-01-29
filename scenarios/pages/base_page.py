from selenium.webdriver.common.by import By

from framework.elements.label import Label


class BasePage:
    """Class to describe base page"""

    PAGE_LOC_TEMPLATE: str = "//div[@class='main-header' and text()='{}']"

    def __init__(self, name):
        """
        Initialize object of a page
        :arg:
         - name: name of a page
        """
        self.name = name
        self.title_label = Label((By.XPATH, self.PAGE_LOC_TEMPLATE.format(name)), 'Title')

    def is_page_opened(self) -> bool:
        """
        Checks if page opened
        :returns: True if page opened
        """
        return self.title_label.is_displayed()
