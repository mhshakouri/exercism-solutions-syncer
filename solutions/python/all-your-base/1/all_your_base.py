def rebase(input_base, digits, output_base):
    # ----- Validate bases -----
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # ----- Handle empty list case -----
    if not digits:
        return [0]

    # ----- Validate digits -----
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # ----- Remove leading zeros -----
    # (But keep a single zero if the number is zero)
    i = 0
    while i < len(digits) - 1 and digits[i] == 0:
        i += 1
    digits = digits[i:]

    # ----- Convert from input_base → integer -----
    value = 0
    for d in digits:
        value = value * input_base + d

    # ----- Special case: the number is zero -----
    if value == 0:
        return [0]

    # ----- Convert integer → output_base digits -----
    out = []
    while value > 0:
        out.append(value % output_base)
        value //= output_base

    # Digits were collected reversed
    return out[::-1]
