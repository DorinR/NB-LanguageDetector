

class MaxList:
    def __init__(self):
        self.data = []

    # special insert that makes sure that the first item in the list
    # is the language with the highest score
    # (a type of priority queue but you can only get the highest value item once.)
    def insert(self, score_tuple: (str, float)):
        if len(self.data):
            if score_tuple[1] > self.data[0][1]:
                self.data.insert(0, score_tuple)
            else:
                self.data.append(score_tuple)
        else:
            self.data.append(score_tuple)

    def get_most_likely_language(self) -> str:
        return self.data[0][0]

    def get_max_score(self):
        return self.data[0][1]
