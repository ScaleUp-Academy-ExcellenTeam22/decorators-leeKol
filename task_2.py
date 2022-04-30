from functools import wraps
from typing import Any, Callable


def surprise_decorator(func: Callable) -> Callable:
    """
    The function is a decorator which get a function and returns a wrapper function for the function it got.
    :param func: The function to be wrapped.
    :return: A wrapper function for the function that was got.
    """
    @wraps(func)
    def print_surprise(*args: Any, **kwargs) -> None:
        """
        The function is a wrapper which gets parameters but does not use them.
        It prints "surprise!".
        :param args: The parameters that the wrapped function gets. It does not use it.
        :param kwargs: The parameters that the wrapped function gets. It does not use it.
        :return: None.
        """
        print("surprise!")
    return print_surprise


@surprise_decorator
def times2(num: int) -> int:
    """
        The function gets a number and returns it multiplied by 2.
        :param num: The number to be multiplied.
        :return: The number that was got, multiplied by 2.
    """
    return num * 2


if __name__ == '__main__':
    times2(3)
