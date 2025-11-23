def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace('-', '')
    
    # Check length (must be 10 characters)
    if len(isbn) != 10:
        return False
    
    # Check that first 9 characters are digits
    if not isbn[:9].isdigit():
        return False
    
    # Check that last character is a digit or 'X'
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False
    
    # Calculate checksum
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    
    # Add check digit (X = 10)
    check_digit = 10 if isbn[9] == 'X' else int(isbn[9])
    total += check_digit * 1
    
    # Valid if total mod 11 == 0
    return total % 11 == 0