from model import Model
from string import ascii_letters, ascii_lowercase

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


def initialize_distribution(vocab: int):
    distribution = {}
    for lang in languages:
        distribution[lang] = {}

    if vocab == 1:
        for key in distribution:
            for letter in ascii_lowercase:
                distribution[key][letter] = 0
    elif vocab == 2:
        for key in distribution:
            for letter in ascii_letters:
                distribution[key][letter] = 0
    else:
        print('the third one hasn\'t been implemented yet')

    return distribution
