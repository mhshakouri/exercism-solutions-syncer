def square_root(number):
    if number < 1:
        raise ValueError("number must be positive")

    if number == 1:
        return 1

    low, high = 1, number

    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid

        if sq == number:
            return mid
        elif sq < number:
            low = mid + 1
        else:
            high = mid - 1

    # Should never reach here if input is guaranteed to have integer square root
    raise ValueError("no integer square root")
