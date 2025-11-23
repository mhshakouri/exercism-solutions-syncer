def is_isogram(string):
    # Convert to lowercase and filter only letters
    letters = [char.lower() for char in string if char.isalpha()]
    # An isogram has all unique letters
    return len(letters) == len(set(letters))