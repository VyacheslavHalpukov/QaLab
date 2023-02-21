import enum
from enum import IntEnum


@enum.unique
class SubmittedTableRow(IntEnum):
    """Enum class to match row names with their numbers"""
    full_name = 0
    email = 1
    gender = 2
    mobile = 3
    birthdate = 4
    subjects = 5
    hobbies = 6
    file_name = 7
    address = 8
    state_city = 9
