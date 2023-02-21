from framework.elements.base_element import BaseElement
from framework.logger.logger import Logger
from framework.utils.browser_utils import Browser


class Multiple(BaseElement):
    """Class to handle a group of checkboxes"""

    def select_value_by_index(self, index: int) -> str:
        """
        Select a checkbox from the group
        :arg:
        - index: int index of the checkbox
        :return: selected value
        """
        Logger.info(f'Select checkbox from group by index: {index}')
        elements = Browser.find_elements(self._locator)
        selected_element = elements[index].text
        elements[index].click()
        return selected_element
