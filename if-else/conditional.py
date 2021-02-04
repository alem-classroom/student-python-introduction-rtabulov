def is_positive(num):
    return num > 0


def is_even(num):
    return num % 2 == 0


def is_positive_and_even(num):
    return is_positive(num) and is_even(num)


def is_positive_or_even(num):
    return is_positive(num) or is_even(num)
