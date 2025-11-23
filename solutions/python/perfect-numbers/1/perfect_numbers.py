def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    # Check if number is a positive integer
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Calculate sum of divisors (excluding the number itself)
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    
    # Classify based on aliquot sum
    if divisor_sum == number:
        return "perfect"
    elif divisor_sum > number:
        return "abundant"
    else:
        return "deficient"