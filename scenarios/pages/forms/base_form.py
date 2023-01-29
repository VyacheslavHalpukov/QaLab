from selenium.webdriver.common.by import By

from framework.elements.label import Label


class BaseForm:
    """Base form class"""

    def __init__(self, uniq_element: tuple[By, str], name: str):
        """
        Initialization of BaseForm
        :arg:
         - name: title of the form
        """
        self.name = name
        self.uniq_element = Label(uniq_element, name)

    def is_displayed(self) -> bool:
        """
        Checks if form displayed
        :returns: True if form is displayed
        """
        return self.uniq_element.is_displayed()
