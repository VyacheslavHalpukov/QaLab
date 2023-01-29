from selenium.webdriver.common.by import By

from framework.elements.table import Table
from scenarios.pages.forms.base_form import BaseForm


class SubmittedForm(BaseForm):
    """Submitted form of automation practice"""

    TABLE_LOCATOR: tuple[By.XPATH, str] = (By.XPATH, '//div[@class="table-responsive"]//tbody/tr/td[2]')

    def __init__(self):
        """Initialize Submitted form"""
        super().__init__(
            uniq_element=(By.XPATH, '//div[contains(text(),"Thanks for submitting the form")]'),
            name='Submitted Form')

    def read_table(self) -> list:
        """
        Read data from table
        :returns: list of data from table
        """
        table = Table(self.TABLE_LOCATOR, 'Automation practice table')
        return table.get_table_data()
