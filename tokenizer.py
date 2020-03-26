from typing import List
from string import ascii_lowercase, ascii_letters


def tokenize(vocab_type: int, text: str) -> str:
    """Tokeninzer designed specifically for Unigram Classifier because we are not keeping track of out-of-vocab character existence"""
    if vocab_type == 1:
        token_list = [c for c in text if c in ascii_lowercase]
        tokens = ''.join(token_list)
    elif vocab_type == 2:
        token_list = [c for c in text if c in ascii_letters]
        tokens = ''.join(token_list)
    else:
        # check if the isprintable needs to be changed to something else based on prof's response
        token_list = [c for c in text if c.isalpha()]
        tokens = ''.join(token_list)

    return tokens
