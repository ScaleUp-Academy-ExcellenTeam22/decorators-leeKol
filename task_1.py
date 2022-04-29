from functools import wraps
from typing import Any, Callable


def type_check(correct_type: type) -> Callable:
    """
        The function is a decorator factory which returns decorators that decorate functions with one argument and check
        if the parameter the function receives is of the correct type.
        :param correct_type: The correct type for the function's parameter.
        :return: A custom type-checker decorator.
    """
    def custom_type_checker(func: Callable) -> Callable:
        """
            The function is a decorator which get a function and returns a wrapper function for the function it got.
            :param func: The function to be wrapped.
            :return: A wrapper function for the function that was got.
        """
        @wraps(func)
        def check_type(parameter: Any) -> Any:
            """
                The function is a wrapper which gets a parameter and checks if it is of the correct type.
                If it is, it calls the function it wraps with this parameter and returns the result,
                and if it is wrong, it raises a TypeError exception.
                :param parameter: The parameter whose type will be checked.
                :return: The value that the wrapped function returned
            """
            if isinstance(parameter, correct_type):
                return func(parameter)
            else:
                raise TypeError
        return check_type
    return custom_type_checker


@type_check(int)
def times2(num: int) -> int:
    """
        The function gets a number and returns it multiplied by 2.
        :param num: The number to be multiplied.
        :return: The number that was got, multiplied by 2.
    """
    return num * 2
