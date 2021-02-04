def is_positive(num):
    if (num > 0):
        return True
    return False


def is_even(num):
    if (num / 2 == 0):
        return True
    return False


def is_positive_and_even(num):
    return is_positive(num) and is_even(num)


def is_positive_or_even(num):
    return is_positive(num) or is_even(num)
