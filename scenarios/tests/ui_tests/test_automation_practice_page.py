from scenarios.models.automation_practice_model import AutomationPracticeModel
from scenarios.pages.automation_practice_page import AutomationPracticePage
from scenarios.pages.forms.submitted_form import SubmittedForm
from scenarios.steps.ui_steps.automation_practice_page_steps import AutomationPracticePageSteps
from scenarios.steps.ui_steps.common_steps import CommonSteps
from scenarios.steps.ui_steps.submitted_form_steps import SubmittedFormSteps


class TestAutomationPracticePage:

    def test_automation_practice_page_data_match_submitted_form(self, ui_with_automation_page):
        """Test fills in the form with data and checks if the data is correct"""
        data = AutomationPracticeModel.get_random_automation_practice_model()
        automation_page_steps = AutomationPracticePageSteps(AutomationPracticePage())
        CommonSteps.assert_automation_practice_page_opened()
        automation_page_steps.filling_automation_practice_form(data)

        CommonSteps.assert_submitted_form_opened()
        submitted_form_steps = SubmittedFormSteps(SubmittedForm())
        submitted_form_steps.assert_data_in_form(data)
