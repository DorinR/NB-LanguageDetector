

class MaxList:
    def __init__(self):
        self.data = []

    def insert(self, score_tuple: (str, float)):
        if len(self.data):
            if score_tuple[1] > self.data[0][1]:
                self.data.insert(0, score_tuple)
            else:
                self.data.append(score_tuple)
        else:
            self.data.append(score_tuple)

    def get_max_score(self) -> str:
        return self.data[0][0]
