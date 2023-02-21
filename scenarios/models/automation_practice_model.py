from faker import Faker


class AutomationPracticeModel:
    """class describes automation practice form model"""

    def __init__(self, **kwargs):
        """Initialize automation practice form model
        :arg:
        - kwargs: first and last names, email, gender, phone, date of birth, subjects, hobbies, file, state, city
        """
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.email = kwargs['email']
        self.gender = kwargs['gender']
        self.mobile = kwargs['mobile']
        self.birthdate = kwargs['birthdate']
        self.subjects = kwargs['subjects']
        self.hobbies = kwargs['hobbies']
        self.file_name = kwargs['file_name']
        self.address = kwargs['address']
        self.state = kwargs['state']
        self.city = kwargs['city']

    @staticmethod
    def get_random_automation_practice_model():
        """
        Get a random AutomationPracticeModel instance with fake data
        :return: AutomationPracticeModel instance with random data
        """
        fake = Faker()
        random_date = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'gender': fake.random_element([0, 1, 2]),
            'mobile': str(fake.random_number(digits=10)),
            'birthdate': fake.date_of_birth().strftime("%d %B,%Y"),
            'subjects': fake.random_elements(['English', 'Hindi', 'Physics'], length=1)[0],
            'hobbies': fake.random_element([0, 1, 2]),
            'file_name': 'test.txt',
            'address': fake.address().replace("\n", ", "),
            'state': '',
            'city': '',
        }
        return AutomationPracticeModel(**random_date)
