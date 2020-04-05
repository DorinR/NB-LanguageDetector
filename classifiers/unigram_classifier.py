from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model
from tokenizer import tokenize
from distribution_initializer import initialize_distribution
from math import log10
from data_structures.max_list import MaxList

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


class UnigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Unigram Classifier...')
        self.distribution = initialize_distribution()

        # count characters in all training tweets
        for tweet in self.training_data:
            tweet_characters = tokenize(self.model.vocabulary, tweet.text)
            for char in tweet_characters:
                if char in self.distribution[tweet.lang]:
                    self.distribution[tweet.lang][char] += 1
                else:
                    self.distribution[tweet.lang][char] = 1

        # count total letters for each language
        for language in self.distribution:
            total_letter_count = 0
            for letter in self.distribution[language]:
                total_letter_count += self.distribution[language][letter]
            self.distribution[language]["total"] = total_letter_count

        # add delta smoothing
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] += self.model.delta

        # count total number of tokens in all languages (used for computing p(lang))
        total_tokens = 0
        for language in self.distribution:
            total_tokens += self.distribution[language]['total']
        for language in self.distribution:
            self.distribution[language]['p_language'] = self.distribution[language]['total']/total_tokens

        # compute probabilities of each letter in each language
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] = self.distribution[language][letter] / \
                    self.distribution[language]['total']

    def classify(self):
        print('Unigram Classifier is classifying Test Tweets ...')
        for tweet in self.testing_data:
            language_scores = MaxList()
            tweet_letters = tokenize(self.model.vocabulary, tweet.text)
            for language in languages:
                tweet_score_per_language = 0
                for letter in tweet_letters:
                    try:
                        tweet_score_per_language += log10(
                            self.distribution[language][letter])
                    except:
                        if self.model.delta:
                            tweet_score_per_language += log10(self.model.delta)
                        else:
                            continue
                tweet_score_per_language += log10(
                    self.distribution[language]['p_language'])
                language_scores.insert((language, tweet_score_per_language))
            tweet.language_scores = language_scores
