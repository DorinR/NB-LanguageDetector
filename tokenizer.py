from typing import List
from string import ascii_lowercase, ascii_letters
from string import ascii_lowercase, ascii_letters
import string


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


def get_n_grams(text: str, vocab_type: int, n: int) -> List[str]:
    # pre-processing string, to replace out-of-vocabulary characters with *'s
    if vocab_type == 1:
        text = text.lower()
        text = ''.join(
            [c if c in ascii_lowercase else '*' for c in text])
    elif vocab_type == 2:
        text = ''.join(
            [c if c in ascii_letters else '*' for c in text])
    else:
        text = ''.join(
            [c if c.isalpha() else '*' for c in text])

    # formation of bigrams
    n_gram = [text[i:i+n]
              for i, c in enumerate(text) if len(text[i:i+n]) == n and '*' not in text[i:i+n]]

    return n_gram
