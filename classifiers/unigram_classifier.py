from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model


class UnigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Unigram Classifier...')
        self.distribution = 'unigram distribution'

    def classify(self):
        print('Unigram classifier is classifying test tweets...')
