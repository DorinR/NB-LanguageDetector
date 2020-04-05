from model import Model
from string import ascii_letters, ascii_lowercase
from typing import List

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


def initialize_distribution():
    distribution = {}
    for lang in languages:
        distribution[lang] = {}

    return distribution
