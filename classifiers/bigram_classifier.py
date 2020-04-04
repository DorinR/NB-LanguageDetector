from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model
from distribution_initializer import initialize_distribution
from tokenizer import get_n_grams
from helpers.smoothing_extra import get_smoothing_extra
from data_structures.max_list import MaxList
from math import log10

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


class BigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Bigram Classifier...')
        self.distribution = initialize_distribution(self.model.vocabulary)
        # add counts to the dictionary
        for tweet in self.training_data:
            tweet_bigrams = get_n_grams(
                tweet.text, self.model.vocabulary, self.model.n_gram_size)
            for bigram in tweet_bigrams:
                if bigram not in self.distribution[tweet.lang]:
                    self.distribution[tweet.lang][bigram] = 1
                else:
                    self.distribution[tweet.lang][bigram] += 1

        # add delta smoothing to each letter currently in dictionary
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] += self.model.delta
        # print(self.distribution)

        # count total letters for each language
        for language in self.distribution:
            total_token_count = 0
            for bigram in self.distribution[language]:
                total_token_count += self.distribution[language][bigram]
            smoothing_extra = get_smoothing_extra(
                self.model.vocabulary, self.model.n_gram_size, len(self.distribution[language]))
            self.distribution[language]["total"] = total_token_count + \
                smoothing_extra
        # print('Dictionary with smoothing and totals:')
        # print(self.distribution)

        # count total number of tokens in all languages (used for computing p(lang))
        total_tokens = 0
        for language in self.distribution:
            total_tokens += self.distribution[language]['total']
        for language in self.distribution:
            self.distribution[language]['p_language'] = self.distribution[language]['total']/total_tokens
        # print('Dictionary after computing p_language:')
        # print(self.distribution)

        # compute probabilities of each bigram in each language
        for language in self.distribution:
            for bigram in self.distribution[language]:
                self.distribution[language][bigram] = self.distribution[language][bigram] / \
                    self.distribution[language]['total']
        # print('Final character probability distribution after training: ')
        # print(self.distribution)

    def classify(self):
        print('Bigram classifier is classifying test tweets...')
        for tweet in self.testing_data:
            language_scores = MaxList()
            tweet_bigrams = get_n_grams(
                tweet.text, self.model.vocabulary, self.model.n_gram_size)
            for language in languages:
                tweet_score_per_language = 0
                for bigram in tweet_bigrams:
                    try:
                        tweet_score_per_language += log10(
                            self.distribution[language][bigram])
                    except:
                        if self.model.delta:
                            tweet_score_per_language += log10(self.model.delta)
                        else:
                            continue
                tweet_score_per_language += self.distribution[language]['p_language']
                language_scores.insert((language, tweet_score_per_language))
            tweet.language_scores = language_scores
        # testing
        # correct = 0
        # total = 0
        # for score in self.testing_data[0].language_scores.data:
        #     print(score)
        # print(self.testing_data[0].language_scores.get_max_score())
        # for i in range(len(self.testing_data)):
        #     total += 1
        #     if self.testing_data[i].language_scores.get_most_likely_language() == self.testing_data[i].lang:
        #         correct += 1
        #     print(
        #         f'Tweet #{i+1}: Classified as: {self.testing_data[i].language_scores.get_most_likely_language()}. Actual category: {self.testing_data[i].lang}')
        # print(f'got {correct} out of {total} right')
