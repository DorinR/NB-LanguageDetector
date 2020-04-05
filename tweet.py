class Tweet:
    def __init__(self, id: int, user: str, lang: str, text: str):
        self.id = id
        self.user = user
        self.lang = lang
        self.text = text
        self.language_scores = None

    # used for testing
    def print_data_old(self):
        print('======< Tweet Data: START >======')
        print(f'ID: {self.id}')
        print(f'user: {self.user}')
        print(f'lang: {self.lang}')
        print(f'text: {self.text}')
        print('======< Tweet Data: END >======')

    # used for testing
    def print_data(self):
        print(f'Tweet => {self.id} {self.user} {self.lang} {self.text}')
