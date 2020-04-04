from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model
from tokenizer import tokenize
from distribution_initializer import initialize_distribution_unigram
from math import log10
from data_structures.max_list import MaxList

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


class UnigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Unigram Classifier...')
        self.distribution = initialize_distribution_unigram(
            self.model.vocabulary)

        # count characters in all training tweets
        for tweet in self.training_data:
            tweet_characters = tokenize(self.model.vocabulary, tweet.text)
            print(tweet_characters)
            for char in tweet_characters:
                self.distribution[tweet.lang][char] += 1
        # print('Dictionary after counting characters in training set:')
        # print(self.distribution)

        # add delta smoothing
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] += self.model.delta
        # print('Dictionary after adding delta smoothing:')
        # print(self.distribution)

        # count total letters for each language
        for language in self.distribution:
            total_letter_count = 0
            for letter in self.distribution[language]:
                total_letter_count += self.distribution[language][letter]
            self.distribution[language]["total"] = total_letter_count
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

        # compute probabilities of each letter in each language
        for language in self.distribution:
            for letter in self.distribution[language]:
                self.distribution[language][letter] = self.distribution[language][letter] / \
                    self.distribution[language]['total']
        print('Final character probability distribution after training: ')
        print(self.distribution)

    def classify(self):
        print('Unigram Classifier is classifying Test Tweets ...')
        for tweet in self.testing_data:
            language_scores = MaxList()
            tweet_letters = tokenize(self.model.vocabulary, tweet.text)
            for language in languages:
                tweet_score_per_language = 0
                for letter in tweet_letters:
                    tweet_score_per_language += log10(
                        self.distribution[language][letter])
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
        #     if self.testing_data[i].language_scores.get_max_score() == self.testing_data[i].lang:
        #         correct += 1
        #     # print(
        #     #     f'Tweet #{i+1}: Classified as: {self.testing_data[i].language_scores.get_max_score()}. Actual category: {self.testing_data[i].lang}')
        # print(f'got {correct} out of {total} right')
