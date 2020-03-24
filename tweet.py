class Tweet:
    def __init__(self, id: int, user: str, lang: str, text: str):
        self.id = id
        self.user = user
        self.lang = lang
        self.text = text

    def print_data(self):
        print('======Tweet data======')
        print(f'ID: {self.id}')
        print(f'user: {self.user}')
        print(f'lang: {self.lang}')
        print(f'text: {self.text}')
