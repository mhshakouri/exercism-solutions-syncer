def is_pangram(sentence):
    letters = set(char.lower() for char in sentence if char.isalpha())
    return len(letters) == 26