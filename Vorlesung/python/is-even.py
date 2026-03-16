def is_even(number):
    assert isinstance(number ,int) and number >=1, "keine positive natürliche zahl"

    if number % 2:
        return False
    else:
        return True


assert not is_even(9)
assert is_even(10)
assert is_even(-1)
