class LeftParagraph:
    def __init__(self, width: int):
        self.width = width
        self.text = ['']
    
    def add_word(self, word: str):
        if len(self.text[-1] + ' ' + word) <= self.width:
            self.text[-1] += ' ' + word if self.text[-1] else word
        else:
            self.text.append(word)

    def end(self):
        print('\n'.join(self.text))

class RightParagraph:
    def __init__(self, width: int):
        self.width = width
        self.text = ['']
    
    def add_word(self, word: str):
        if len(self.text[-1] + ' ' + word) <= self.width:
            self.text[-1] += ' ' + word if self.text[-1] else word
        else:
            self.text.append(word)

    def end(self):
        print('\n'.join(map(lambda line: line.rjust(self.width), self.text)))
