class MinMaxWordFinder:
    def __init__(self):
        self.words = list()

    def add_sentence(self, string: str):
        self.words += string.split()

    def shortest_words(self):
        return sorted(filter(lambda word: len(word) == len(min(self.words, key=len)), self.words))

    def longest_words(self):
        return sorted(set(filter(lambda word: len(word) == len(max(self.words, key=len)), self.words)))
