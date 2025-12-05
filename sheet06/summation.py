def get_summation_sq(number):
    assert isinstance(number, int) and number >= 1, (
        "Die gegebene Zahl ist keine positive, natürliche Zahl."
    )

    result = 0

    for k in range(1, number + 1):
        result += k * k

    return result


def get_summation_sq_test(number):
    assert isinstance(number, int) and number >= 1, (
        "Die gegebene Zahl ist keine positive, natürliche Zahl."
    )

    return (number * (number + 1) * (2 * number + 1)) / (6)


assert get_summation_sq(1) == get_summation_sq_test(1)
assert get_summation_sq(3) == get_summation_sq_test(3)
assert get_summation_sq(5) == get_summation_sq_test(5)
