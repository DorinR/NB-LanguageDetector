from classifiers.abstract_classifier import AbstractClassifier
from typing import List
from tweet import Tweet
from model import Model


class TrigramClassifier(AbstractClassifier):
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        super().__init__(model, training_data, testing_data)

    def train(self):
        print('Training Trigram Classifier...')
        self.distribution = 'trigram distribution'

    def classify(self):
        print('Trigram classifier is classifying test tweets...')
