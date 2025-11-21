VOWELS = "aeiou"
SPECIAL_PREFIXES = ["xr", "yt"]
SUFFIX = "ay"

def starts_with_vowel(word):
    return word[0].lower() in VOWELS
    
def starts_with_special(word):
    return any(word.lower().startswith(prefix) for prefix in SPECIAL_PREFIXES)

def starts_with_qu(word):
    return word.lower().startswith("qu")

def has_qu_after_consonant(word):
    # Returns idx if "qu" follows a consonant cluster at the start, otherwise None
    idx = word.find("qu")
    if idx > 0:
        # all before "qu" should be consonants
        if all(c.lower() not in VOWELS for c in word[:idx]):
            return idx
    return None

def y_as_vowel_index(word):
    # Returns index of 'y' when it acts as a vowel, not at start
    for i, c in enumerate(word):
        if c.lower() == "y" and i != 0:
            return i
    return None

def consonant_cluster_index(word):
    for i, c in enumerate(word):
        if c.lower() in VOWELS:
            return i
    for i, c in enumerate(word):
        if c.lower() == "y" and i != 0:
            return i
    return None

def pig_latin_word(word):
    # Rule 1: Vowel start or special prefix
    if starts_with_vowel(word) or starts_with_special(word):
        return word + SUFFIX

    # Rule 2: Starts with 'qu'
    if starts_with_qu(word):
        return word[2:] + word[:2] + SUFFIX

    # Rule 3: Cluster followed by 'qu'
    qu_idx = has_qu_after_consonant(word)
    if qu_idx:
        return word[qu_idx+2:] + word[:qu_idx+2] + SUFFIX

    # Default: Cluster before first vowel or "y"
    idx = consonant_cluster_index(word)
    if idx:
        return word[idx:] + word[:idx] + SUFFIX

    # Edge case – no vowel/y-as-vowel found, just add suffix
    return word + SUFFIX

def translate(text):
    return " ".join(pig_latin_word(word) for word in text.split())
