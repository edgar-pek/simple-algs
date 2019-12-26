
def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
        number(int): Number to find floored squared root of
    Returns:
        int: Floored Square Root
        special case: number < 0 or number is not an integer returns -1
    """
    if not isinstance(number, int):
        # print("Expected non-negative integer as input")
        return -1
    if number < 0:
        # print("Expecting non-negative integer")
        return -1
    if number < 2:
        return number
    lo = 2
    hi = (number >> 5) + 8  # choice of hi will be explained in the text file
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        if mid * mid > number:
            hi = mid - 1
        else:
            lo = mid + 1
    assert lo == (hi + 1)
    return lo - 1


# added corner cases
assert sqrt(-1) == -1
print(sqrt(-1))
# expected output: -1
assert sqrt(None) == -1
print(sqrt(-1))
# expected output: -1
assert sqrt([]) == -1
print(sqrt(-1))
# expected output: -1
assert sqrt(float("inf")) == -1
print(sqrt(-1))
# expected output: -1
assert sqrt(256) == 16
print(sqrt(256))
# expected output: 16

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
