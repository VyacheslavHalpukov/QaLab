from selenium.webdriver.common.by import By

from framework.elements.base_element import BaseElement
from framework.logger.logger import Logger
from framework.utils.browser_utils import Browser


class DropDown(BaseElement):
    """Class realize actions with drop down element"""

    def __init__(self, locator: tuple[By, str], name: str, items: tuple[By, str]):
        """
        Initialize drop down element
        :args:
         - locator: tuple(By, value)
         - name: name of element
         - items: list of items in the dropdown
        """
        super().__init__(locator, name)
        self._items = items

    def select_item_by_index(self, index: int) -> str:
        """
        Select an item from the dropdown
        :arg:
        - index: int index of the item
        :returns: Selected value
        """
        Logger.info(f'Select item from drop drown by index: {index}')
        elements = Browser.find_elements(self._items)
        selected_element = elements[index].text
        elements[index].click()
        return selected_element

    def get_item_count(self) -> int:
        """
        Return the number of items in the dropdown
        :return: numbers of items
        """
        Logger.info(f'Get number items: {len(self._items)}')
        return len(self._items)
