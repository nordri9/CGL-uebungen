def is_even(number):
    assert isinstance(number, int) and number >= 1, (
        "Die gegebene Zahl ist keine positive, natürliche Zahl."
    )

    if number % 2 == 0:
        return True

    else:
        return False


assert not is_even(9)
assert is_even(10)
assert is_even(-1)
