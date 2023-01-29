from framework.utils.random_utils import RandomUtils
from scenarios.models.automation_practice_model import AutomationPracticeModel
from scenarios.pages.automation_practice_page import AutomationPracticePage


class AutomationPracticePageSteps:
    """Class to describe steps on the automation practice page"""

    def __init__(self, automation_practice_page: AutomationPracticePage):
        """Initialize steps class instance"""
        self.page = automation_practice_page

    def filling_automation_practice_form(self, data: AutomationPracticeModel) -> None:
        """Steps filling automation practice form"""
        self.page.enter_first_name(data.first_name)
        self.page.enter_last_name(data.last_name)
        self.page.enter_email(data.email)
        data.gender = self.page.select_gender(data.gender)
        self.page.enter_mobile(data.mobile)
        self.page.enter_birthday(data.birthdate)
        self.page.enter_subjects(data.subjects[0])
        data.hobbies = self.page.select_hobbies(data.hobbies)
        self.page.attached_file(data.file_name)
        self.page.enter_address(data.address)
        state = self.page.state_dropdown()
        state.click()
        data.state = state.select_item_by_index(RandomUtils.get_random_int_value(state.get_item_count() - 1))
        city = self.page.city_dropdown()
        city.click()
        data.city = city.select_item_by_index(RandomUtils.get_random_int_value(city.get_item_count() - 1))
        self.page.click_submit_button()
