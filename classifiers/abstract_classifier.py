from model import Model
from tweet import Tweet
from typing import List
import os.path

languages = ['eu', 'ca', 'gl', 'es', 'en', 'pt']


class AbstractClassifier:
    def __init__(self, model: Model, training_data: List[Tweet], testing_data: List[Tweet]):
        self.model = model
        self.training_data = training_data
        self.testing_data = testing_data
        self.distribution = {}
        self.accuracy = None
        self.per_class_precision = None
        self.per_class_recall = None
        self.per_class_f1 = None
        self.macro_f1 = None
        self.weighted_average_f1 = None

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
        print('Saving Evaluation Results ...')
        data_to_write_to_file = []
        # compose filename
        filename = f'eval_{self.model.vocabulary}_{self.model.n_gram_size}_{self.model.delta}.txt'
        data_to_write_to_file.append(filename)
        # add accuracy
        data_to_write_to_file.append(self.accuracy)
        # compose per-class precision line
        per_class_precision = []
        for class_ in self.per_class_precision:
            per_class_precision.append(str(self.per_class_precision[class_]))
        per_class_precision_string = "  ".join(per_class_precision)
        data_to_write_to_file.append(per_class_precision_string)
        # compose per-class recall line
        per_class_recall = []
        for class_ in self.per_class_recall:
            per_class_recall.append(str(self.per_class_recall[class_]))
        per_class_recall_string = "  ".join(per_class_recall)
        data_to_write_to_file.append(per_class_recall_string)
        # compose per-class f1 measure line
        per_class_f1 = []
        for class_ in self.per_class_f1:
            per_class_f1.append(str(self.per_class_f1[class_]))
        per_class_f1_string = "  ".join(per_class_f1)
        data_to_write_to_file.append(per_class_f1_string)
        # compose macro-F1 and weighted-average-f1 line
        macros = []
        macros_string = f'{self.macro_f1}  {self.weighted_average_f1}'
        data_to_write_to_file.append(macros_string)
        # write it all to file
        self.write_to_file(data_to_write_to_file)

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
        # print(f'Accuracy is {self.accuracy}')

    def compute_per_class_precision(self):
        class_precisions = {}
        for language in languages:
            tp = 0
            tp_plus_fp = 0
            for tweet in self.testing_data:
                if tweet.language_scores.get_most_likely_language() == language:
                    tp_plus_fp += 1
                    if tweet.lang == language:
                        tp += 1
            class_precisions[language] = tp/tp_plus_fp
        self.per_class_precision = class_precisions
        # print(f'Per-Class Precision is: {self.per_class_precision}')

    def compute_per_class_recall(self):
        class_recalls = {}
        for language in languages:
            tp = 0
            tp_plus_fn = 0
            for tweet in self.testing_data:
                if tweet.lang == language:
                    tp_plus_fn += 1
                    if tweet.language_scores.get_most_likely_language() == language:
                        tp += 1
            class_recalls[language] = tp/tp_plus_fn
        self.per_class_recall = class_recalls
        # print(f'Per-Class Recall is: {self.per_class_recall}')

    def compute_per_class_f1(self):
        class_f1 = {}
        for language in languages:
            try:
                class_f1[language] = (2*self.per_class_precision[language]*self.per_class_recall[language])/(
                    self.per_class_precision[language]+self.per_class_recall[language])
            except:
                class_f1[language] = 0
        self.per_class_f1 = class_f1
        # print(f'Per-Class F1 is: {self.per_class_f1}')

    def compute_macro_f1(self):
        total_f1 = 0
        for language in self.per_class_f1:
            total_f1 += self.per_class_f1[language]
        self.macro_f1 = total_f1/len(self.per_class_f1)
        # print(f'Macro F1 is: {self.macro_f1}')

    def compute_weighted_average_f1(self):
        weighted_f1 = 0
        for language in self.per_class_f1:
            weighted_f1 += self.distribution[language]['p_language'] * \
                self.per_class_f1[language]
        self.weighted_average_f1 = weighted_f1
        # print(f'Weighted F1 is: {self.weighted_average_f1}')

    def evaluate(self):
        self.compute_accuracy()
        self.compute_per_class_precision()
        self.compute_per_class_recall()
        self.compute_per_class_f1()
        self.compute_macro_f1()
        self.compute_weighted_average_f1()

    def print_data(self):
        """method used for testing"""
        print('======< Classifier Data: START >======')
        # print(f'model: {self.model.print_data()}')
        self.training_data[0].print_data()
        self.testing_data[0].print_data()
        print(f'distribution: {self.distribution}')
        print('======< Classifier Data: END >======')
