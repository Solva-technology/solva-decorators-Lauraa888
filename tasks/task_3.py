from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in list(args) + list(kwargs.values()):
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args, **kwargs)

    return wrapper
