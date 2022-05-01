import decorator
from typing import Any, Callable


@decorator.decorator
def execute_twice(func: Callable, *args: Any, **kwargs: Any) -> tuple:
    """
    The function is a decorator that gets a function and parameters for it, executes the function it wraps twice,
    and returns a tuple containing the two return values of the function.
    :param func: the wrapped function to be executed twice.
    :param args: The parameters that the wrapped function gets. It does not use it.
    :param kwargs: The parameters that the wrapped function gets. It does not use it.
    :return: A tuple containing the two return values of the function.
    """
    return tuple(func(*args, **kwargs) for foo in range(2))


@execute_twice
def times2(num: int) -> int:
    """
    The function gets a number and returns it multiplied by 2.
    :param num: The number to be multiplied.
    :return: The number that was got, multiplied by 2.
    """
    return num * 2


if __name__ == '__main__':
    print(times2(3))
