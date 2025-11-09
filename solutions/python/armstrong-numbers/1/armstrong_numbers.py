def is_armstrong_number(number):
    # Turn the number into a string, so we can look at each digit!
    digits = str(number)
    # Count how many digits are in the number
    n_digits = len(digits)
    # Start with zero, and we will add each digit's magic
    total = 0
    # For each digit in the number...
    for d in digits:
        # Change the digit back into a number, then do the "magic trick":
        # raise it to the power of number of digits, then add it to total
        total += int(d) ** n_digits
    # If our total equals the starting number, it's a magic Armstrong number!
    return total == number