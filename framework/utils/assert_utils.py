class Asserts:

    @staticmethod
    def soft_assert(checks: list[tuple[bool, str]]) -> None:
        """
        Soft assertion for different kinds of comparative functions
        :arg:
         - checks: list of tuples [(expression, error_message)]
        :raises: AssertionError if any check is False
        :using:
         when there is a need to assert some different results without failing test upon first failed check:

         soft_assert([(a == b, 'a is not equal b'), (a != b, 'a equals b')])
        """
        errors = [check[1] for check in checks if not check[0]]

        if errors:
            raise AssertionError('\n'.join(errors))

    @staticmethod
    def assert_true(expression: bool, check_parameter: str) -> None:
        """
        Assertion of result to be True
        :args:
         - expression: function that returns bool value
         - check_parameter: string representation of what expects to be True. Will be part of error message
        """
        assert expression, f'Expected [{check_parameter}] to be True, but was False'
