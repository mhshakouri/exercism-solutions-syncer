def rotate(text, key):
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                shifted = (ord(char) - ord('A') + key) % 26
                result.append(chr(ord('A') + shifted))
            else:
                # Shift lowercase letters
                shifted = (ord(char) - ord('a') + key) % 26
                result.append(chr(ord('a') + shifted))
        else:
            # Keep non-letter characters as is
            result.append(char)
    
    return ''.join(result)