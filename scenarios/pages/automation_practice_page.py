from selenium.webdriver.common.by import By

from framework.elements.attach_file import AttachFile
from framework.elements.dropdown import DropDown
from framework.elements.multiple import Multiple
from framework.elements.textbox import TextBox
from scenarios.pages.base_page import BasePage


class AutomationPracticePage(BasePage):
    """Class to describe automation practice page"""

    FIRST_NAME_FIELD_LOCATOR: tuple[By, str] = (By.ID, 'firstName')
    LAST_NAME_FIELD_LOCATOR: tuple[By, str] = (By.ID, 'lastName')
    EMAIL_FIELD_LOCATOR: tuple[By, str] = (By.ID, 'userEmail')
    GENDER_MULTIPLE_LOCATOR: tuple[By, str] = (By.XPATH, '//div[@id="genterWrapper"]//input[@value]/parent::*')
    MOBILE_FIELD_LOCATOR: tuple[By, str] = (By.ID, 'userNumber')
    DATE_BIRTH_PICKER_LOCATOR: tuple[By, str] = (By.ID, 'dateOfBirthInput')
    SUBJECTS_FIELD_LOCATOR: tuple[By, str] = (By.XPATH, '//div[@id="subjectsContainer"]//input')
    HOBBIES_WRAPPER_LOCATOR: tuple[By, str] = (By.XPATH, '//div[@id="hobbiesWrapper"]//input//parent::*/label')
    UPLOAD_BUTTON_LOCATOR: tuple[By, str] = (By.ID, 'uploadPicture')
    ADDRESS_TEXTAREA_LOCATOR: tuple[By, str] = (By.ID, 'currentAddress')
    STATE_DROPDOWN_LOCATOR: tuple[By, str] = (By.XPATH, '//div[@id="state"]')
    STATE_DROPDOWN_ITEMS: tuple[By, str] = (By.XPATH, '//div[contains(@id, "react-select-3-option")]')
    CITY_DROPDOWN_LOCATOR: tuple[By, str] = (By.ID, 'city')
    CITY_DROPDOWN_ITEMS: tuple[By, str] = (By.XPATH, '//div[contains(@id, "react-select-4-option")]')
    SUBMIT_BUTTON_LOCATOR: tuple[By, str] = (By.ID, 'submit')

    def __init__(self):
        """Initialize Device Page"""
        super().__init__(name='Practice Form')

    def enter_first_name(self, name: str) -> None:
        """
        Enter first name in field
        :arg:
         - name: name for field first name
        """
        TextBox(self.FIRST_NAME_FIELD_LOCATOR, 'First name field').type(name)

    def enter_last_name(self, name: str) -> None:
        """
        Enter last name in field
        :arg:
         - name: name for field last name
        """
        TextBox(self.LAST_NAME_FIELD_LOCATOR, 'Last name field').type(name)

    def enter_email(self, email: str) -> None:
        """
        Enter email in field
        :arg:
         - email: email for field email
        """
        TextBox(self.EMAIL_FIELD_LOCATOR, 'Email field').type(email)

    def enter_mobile(self, mobile: str) -> None:
        """
        Enter mobile in field
        :arg:
         - mobile: mobile number for field mobile
        """
        TextBox(self.MOBILE_FIELD_LOCATOR, 'Mobile field').type(mobile)

    def click_submit_button(self) -> None:
        """
        Click on submit button
        """
        submit_button = TextBox(self.SUBMIT_BUTTON_LOCATOR, 'Submit button')
        submit_button.click()

    def state_dropdown(self) -> DropDown:
        """
        State dropdown
        :return WebElement if present
        """
        return DropDown(self.STATE_DROPDOWN_LOCATOR, 'State drop down', self.STATE_DROPDOWN_ITEMS)

    def city_dropdown(self) -> DropDown:
        """
        City dropdown
        :return WebElement if present
        """
        return DropDown(self.CITY_DROPDOWN_LOCATOR, 'City drop down', self.CITY_DROPDOWN_ITEMS)

    def attached_file(self, file: str) -> None:
        """
        Attach file to the form
        :arg:
        -file: file with data
        :returns: WebElement and file
        """
        AttachFile(self.UPLOAD_BUTTON_LOCATOR, 'Upload button', file).attach_file()

    def select_gender(self, index: int) -> str:
        """
        Select gender
        :args:
        -index
        :returns: Text selected element
        """
        return Multiple(self.GENDER_MULTIPLE_LOCATOR, 'Gender selector').select_value_by_index(index)

    def enter_subjects(self, subjects: str) -> None:
        """
        Enter subjects into the relevant field on the page
        :args:
        - subjects: str of subjects
        """
        field_subject = TextBox(self.SUBJECTS_FIELD_LOCATOR, 'Mobile field')
        field_subject.type(subjects)
        field_subject.finish_auto_complete()

    def select_hobbies(self, index: int) -> str:
        """
        Enter hobbies into the relevant field on the page
        :args:
        -index: index hobbies
        :returns: Text selected element
        """
        return Multiple(self.HOBBIES_WRAPPER_LOCATOR, 'Hobbies selector').select_value_by_index(index)

    def enter_address(self, address: str) -> None:
        """
        Enter the address into the relevant field on the page
        :args:
        -address: address in string
        """
        TextBox(self.ADDRESS_TEXTAREA_LOCATOR, 'Address text area').type(address)

    def enter_birthday(self, birthday: str) -> None:
        """
        Enter the birthday into the relevant field on the page
        :args:
        -birthday: birthday in format "%d %b %Y"
        """
        calendar = TextBox(self.DATE_BIRTH_PICKER_LOCATOR, 'Calendar picker')
        calendar.click()
        calendar.type(birthday, keys_clear=True)
        calendar.finish_auto_complete()
