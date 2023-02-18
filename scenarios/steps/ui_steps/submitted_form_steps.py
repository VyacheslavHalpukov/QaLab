from framework.utils.assert_utils import Asserts
from scenarios.models.automation_practice_model import AutomationPracticeModel
from scenarios.pages.forms.submitted_form import SubmittedForm


class SubmittedFormSteps:
    """Class to describe steps on the submitted form"""

    def __init__(self, submitted_form: SubmittedForm):
        """Initialize steps class instance"""
        self.form = submitted_form

    def assert_data_in_form(self, expected_data: AutomationPracticeModel) -> None:
        """Assert data in submitted form"""
        print('INSERT DATA:')
        print(list(expected_data.__dict__.values()))
        table_data = self.form.read_table()
        print('DATA IN FORM AFTER SUBMIT BUTTON PRESSED:')
        print(table_data)
        prepare_data = [(exp_data == act_data, name) for name, exp_data, act_data in zip(
            expected_data.__dict__.keys(),
            expected_data.__dict__.values(),
            table_data,
        )]
        Asserts.soft_assert(prepare_data)
