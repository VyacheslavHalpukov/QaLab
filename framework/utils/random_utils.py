import random


class RandomUtils:

    @classmethod
    def get_random_int_value(cls, max_int: int, min_int=0) -> int:
        """
        Generates random integer value that differs from the passed check value
        :args:
         - max_value: max integer value to be generated
         - not_include: sequence of integers that should not be returned
        :optional arg:
         - min_value: int -> min integer value to be generated
        :returns: random integer
        """
        return random.randint(min_int, max_int)
