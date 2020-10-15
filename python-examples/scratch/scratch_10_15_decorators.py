from functools import wraps


def print_result(func):
    """
    Print the result of a function before returning it.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")

        return result

    return wrapper


@print_result
def add(a, b):
    """
    This is some documentation for the add function.
    """
    return a + b