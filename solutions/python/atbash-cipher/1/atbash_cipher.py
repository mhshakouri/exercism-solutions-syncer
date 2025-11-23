import string

PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]

TRANS = str.maketrans(PLAIN, CIPHER)


def encode(plain_text):
    # normalize: lowercase + remove punctuation/spaces
    cleaned = []
    for ch in plain_text.lower():
        if ch.isalpha():
            cleaned.append(ch.translate(TRANS))
        elif ch.isdigit():
            cleaned.append(ch)
        # ignore punctuation

    # group into chunks of five
    joined = "".join(cleaned)
    return " ".join(joined[i:i+5] for i in range(len(joined))[::5])


def decode(ciphered_text):
    # remove spaces
    cleaned = ciphered_text.replace(" ", "")
    # translate letters back using same mapping; digits remain unchanged
    return cleaned.translate(TRANS)
