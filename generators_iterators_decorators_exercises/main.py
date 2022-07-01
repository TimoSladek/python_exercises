from functools import wraps

def get_next_multiple(n):
    for x in range(1, 10):
        yield n*x

def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0 or num <= 1:
        return False

    sqr = int(num**0.5)+1

    for x in range(3, sqr, 2):
        if num % x == 0:
            return False
    return True

def get_next_prime():
    for x in range(2, 1000):
        if is_prime(x):
            yield x

def double_result(fn):
    @wraps(fn)
    def wrap_fn(*args, **kwargs):
        return fn(*args, **kwargs) * 2
    return wrap_fn

def only_even_parameters(fn):
    @wraps(fn)
    def wrap_fn(*args, **kwargs):
        if any([arg for arg in args if arg % 2 != 0]):
            return "Please add even numbers!"
        return fn(*args, **kwargs)
    return wrap_fn

def sum_index(arr):
    total = 0
    for idx, value in enumerate(arr):
        total += idx

    return total