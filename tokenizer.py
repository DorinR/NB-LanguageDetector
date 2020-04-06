from typing import List
from string import ascii_lowercase, ascii_letters
from string import ascii_lowercase, ascii_letters
import string


def tokenize(vocab_type: int, text: str) -> str:
    """Tokeninzer designed specifically for Unigram Classifier because we are not keeping track of out-of-vocab character existence"""
    if vocab_type == 0:
        token_list = [c for c in text if c in ascii_lowercase]
        tokens = ''.join(token_list)
    elif vocab_type == 1:
        token_list = [c for c in text if c in ascii_letters]
        tokens = ''.join(token_list)
    else:
        token_list = [c for c in text if c.isalpha()]
        tokens = ''.join(token_list)

    return tokens


def get_n_grams(text: str, vocab_type: int, n: int) -> List[str]:
    # pre-processing string, to replace out-of-vocabulary characters with *'s
    if vocab_type == 0:
        text_lower = text.lower()
        cleaned_text = ''.join(
            [c if c in ascii_lowercase else '*' for c in text_lower])
    elif vocab_type == 1:
        cleaned_text = ''.join(
            [c if c in ascii_letters else '*' for c in text])
    else:
        cleaned_text = ''.join(
            [c if c.isalpha() else '*' for c in text])

    # formation of bigrams
    n_grams = [cleaned_text[i:i+n]
               for i, c in enumerate(cleaned_text) if len(cleaned_text[i:i+n]) == n and '*' not in cleaned_text[i:i+n]]

    return n_grams


def get_x_grams(text: str, n: int) -> List[str]:
    """tokenizer for custom model"""
    # formation of bigrams
    return [text[i:i+n]
            for i, c in enumerate(text) if len(text[i:i+n]) == n]
