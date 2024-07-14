def null_decorator(func):
    return func


@null_decorator
def greet():
    return "Привет!"


# greet = null_decorator(greet)
print(greet())