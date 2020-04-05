from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model
from tokenizer import get_n_grams
from distribution_initializer import initialize_distribution
from helpers.smoothing_extra import get_smoothing_extra
from data_structures.max_list import MaxList
from math import log10

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


class TrigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Trigram Classifier...')
        self.distribution = initialize_distribution()

        # add counts to dictionary
        for tweet in self.training_data:
            tweet_trigrams = get_n_grams(
                tweet.text, self.model.vocabulary, self.model.n_gram_size)
            for trigram in tweet_trigrams:
                if trigram not in self.distribution[tweet.lang]:
                    self.distribution[tweet.lang][trigram] = 1
                else:
                    self.distribution[tweet.lang][trigram] += 1

        # count total letters for each language
        for language in self.distribution:
            total_token_count = 0
            for trigram in self.distribution[language]:
                total_token_count += self.distribution[language][trigram]
            smoothing_extra = get_smoothing_extra(
                self.model.vocabulary, self.model.n_gram_size, self.model.delta)
            self.distribution[language]["total"] = total_token_count + \
                smoothing_extra

        # add delta smoothing to each letter currently in dictionary
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] += self.model.delta

        # count total number of tokens in all languages (used for computing p(lang))
        total_tokens = 0
        for language in self.distribution:
            total_tokens += self.distribution[language]['total']
        for language in self.distribution:
            self.distribution[language]['p_language'] = self.distribution[language]['total']/total_tokens

        # compute probabilities of each bigram in each language
        for language in self.distribution:
            for trigram in self.distribution[language]:
                self.distribution[language][trigram] = self.distribution[language][trigram] / \
                    self.distribution[language]['total']

    def classify(self):
        print('Trigram classifier is classifying test tweets...')
        for tweet in self.testing_data:
            language_scores = MaxList()
            tweet_bigrams = get_n_grams(
                tweet.text, self.model.vocabulary, self.model.n_gram_size)
            for language in languages:
                tweet_score_per_language = 0
                for trigram in tweet_bigrams:
                    try:
                        tweet_score_per_language += log10(
                            self.distribution[language][trigram])
                    except:
                        if self.model.delta:
                            tweet_score_per_language += log10(
                                self.model.delta/self.distribution[language]['total'])
                        else:
                            continue
                tweet_score_per_language += log10(
                    self.distribution[language]['p_language'])
                language_scores.insert((language, tweet_score_per_language))
            tweet.language_scores = language_scores
