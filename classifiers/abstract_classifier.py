from model import Model
from tweet import Tweet
from typing import List


class AbstractClassifier:
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        self.model = model
        self.training_data = training_data
        self.testing_data = testing_data
        self.distribution = None

    def train(self):
        pass

    def classify(self):
        pass

    def print_data(self):
        print('======< Classifier Data: START >======')
        # print(f'model: {self.model.print_data()}')
        self.training_data[0].print_data()
        self.testing_data[0].print_data()
        print(f'distribution: {self.distribution}')
        print('======< Classifier Data: END >======')
