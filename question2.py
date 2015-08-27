# Question 2
import string

def get_missing_letters(sentence):
    alphabet = list(string.ascii_lowercase)
    sentence = sentence.lower()

    for c in sentence:
        if c in alphabet:
            alphabet.pop(alphabet.index(c))

    return "".join(alphabet)