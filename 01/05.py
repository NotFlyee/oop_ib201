class BigBell:
    def __init__(self):
        self.sounds = ['ding', 'dong']

    def sound(self):
        print(self.sounds[0])
        self.sounds = self.sounds[::-1]
