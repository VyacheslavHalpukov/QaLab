from framework.elements.base_element import BaseElement
from framework.utils.browser_utils import Browser
from scenarios.enums.submitted_table_row import SubmittedTableRow


class Table(BaseElement):
    """Class realize actions with table"""

    def get_table_data(self) -> list:
        """
        Get data from table
        :returns: List of data
        """
        table = Browser.find_elements(self._locator)

        data = []
        for i, row in enumerate(table):
            if i == SubmittedTableRow.full_name.value or i == SubmittedTableRow.state_city.value:
                arr = list(row.text)
                index = len(arr) - arr[::-1].index(" ") - 1
                data.append(''.join(arr[:index]))
                data.append(''.join(arr[index + 1:]))
                row.text.split()
            else:
                data.append(row.text)
        return data
