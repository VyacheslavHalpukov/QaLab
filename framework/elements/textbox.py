from typing import Any

from selenium.webdriver import Keys

from framework.elements.base_element import BaseElement
from framework.logger.logger import Logger


class TextBox(BaseElement):
    """Class to realize actions specific to Textbox"""

    def type(self, text: Any, clear=True, keys_clear=False) -> None:
        """
        Type text to textbox
        :arg:
         -text: value that can be converted to str
        :optionals args:
         -clear: bool -> is clearing textbox required by default
         -keys_clear: bool -> is required clear by send_keys. Won't work if clear is False
        """
        Logger.info(f'Clearing {self._type} {self._name} and typing {text}')
        element = self.wait_for_displayed()
        if clear:
            if keys_clear:
                element.click()
                element.send_keys(Keys.LEFT_CONTROL + 'a')
            else:
                element.clear()
        element.send_keys(text)

    def finish_auto_complete(self) -> None:
        """Finish autocomplete press ENTER"""
        Logger.info(f'Finish autocomplete')
        element = self.wait_for_displayed()
        element.send_keys(Keys.ENTER)
