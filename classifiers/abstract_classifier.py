from model import Model
from tweet import Tweet
from typing import List
import os.path


class AbstractClassifier:
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        self.model = model
        self.training_data = training_data
        self.testing_data = testing_data
        self.distribution = {}
        self.accuracy = None
        self.per_class_precision = None

    def train(self):
        pass

    def classify(self):
        pass

    def save(self):
        self.save_trace()
        self.save_eval()

    def save_trace(self):
        print('Saving Classification Results ...')
        data_to_write_to_file = []
        filename = f'trace_{self.model.vocabulary}_{self.model.n_gram_size}_{self.model.delta}.txt'
        data_to_write_to_file.append(filename)
        for tweet in self.testing_data:
            data_to_write_to_file.append(
                f'{tweet.id}  {tweet.language_scores.get_most_likely_language()}  {tweet.language_scores.get_max_score()}  {tweet.lang}  {"correct" if (tweet.language_scores.get_most_likely_language() == tweet.lang) else "wrong"}')
        self.write_to_file(data_to_write_to_file)

    def save_eval(self):
        pass

    def write_to_file(self, data_to_write):
        directory = os.path.join(f'results/{data_to_write.pop(0)}')
        with open(directory, 'w') as f:
            for line in data_to_write:
                f.write("%s\n" % line)

    def compute_accuracy(self):
        correct_classifications = 0
        for tweet in self.testing_data:
            if tweet.lang == tweet.language_scores.get_most_likely_language():
                correct_classifications += 1
        self.accuracy = correct_classifications/len(self.testing_data)

    def compute_per_class_precision(self):
        pass

    def print_data(self):
        """method used for testing"""
        print('======< Classifier Data: START >======')
        # print(f'model: {self.model.print_data()}')
        self.training_data[0].print_data()
        self.testing_data[0].print_data()
        print(f'distribution: {self.distribution}')
        print('======< Classifier Data: END >======')
