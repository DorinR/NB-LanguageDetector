class Model:
    def __init__(self, vocabulary: int, n_gram_size: int, delta: float, training_file: str, testing_file: str):
        self.vocabulary = int(vocabulary)
        self.n_gram_size = int(n_gram_size)
        self.delta = float(delta)
        self.training_file = training_file
        self.testing_file = testing_file

    # used for debugging
    def print_data(self):
        print('======< Model Data: START >======')
        print(f'model vocabulary: {self.vocabulary}')
        print(f'model n-gram size: {self.n_gram_size}')
        print(f'model delta smoothing: {self.delta}')
        print(f'training file: {self.training_file}')
        print(f'testing file: {self.testing_file}')
        print('======< Model Data: END >======')
