from framework.utils.assert_utils import Asserts
from scenarios.pages.automation_practice_page import AutomationPracticePage
from scenarios.pages.forms.submitted_form import SubmittedForm


class CommonSteps:
    """Class for function that perform similar steps"""

    @staticmethod
    def assert_automation_practice_page_opened() -> None:
        """ Asserts automation practice page opened """
        automation_practice_page = AutomationPracticePage()
        Asserts.assert_true(automation_practice_page.is_page_opened(), f'{automation_practice_page.name} opened')

    @staticmethod
    def assert_submitted_form_opened() -> None:
        """ Asserts submitted form opened """
        submitted_form = SubmittedForm()
        Asserts.assert_true(submitted_form.is_displayed(), f'{submitted_form.name} opened')
