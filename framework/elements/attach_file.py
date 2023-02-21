from selenium.webdriver.common.by import By

from framework.elements.base_element import BaseElement
from framework.logger.logger import Logger
from framework.utils.os_utils import OsUtils


class AttachFile(BaseElement):
    """Class to realize action specific for attach file"""

    def __init__(self, locator: tuple[By, str], name: str, file_name: str):
        """
        Initialize attach file element
        :args:
        - locator: tuple(By, value)
        - name: name of element
        - file_name: name file in string
        """
        super().__init__(locator, name)
        self._file_name = file_name

    def attach_file(self) -> None:
        """
        Attach file
        :args:
        - file_name: name file in string
        """
        Logger.info(f'Attach file: {self._file_name}')
        OsUtils.change_dir('../../resources')
        file_path = '{}/{}'.format(OsUtils.get_current_work_dir(), self._file_name)
        element = self.wait_for_clickable()
        element.send_keys(file_path)
