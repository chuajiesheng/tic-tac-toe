class State:
    NEW = 'NEW'
    PLAY = 'PLAY'
    WON = 'WON'

    def __init__(self):
        self.val = self.NEW

    def move(self):
        if self.val is self.NEW:
            self.val = self.PLAY
        else:
            self.val = self.WON

    def is_new(self):
        return self.val == self.NEW

    def is_play(self):
        return self.val == self.PLAY

    def is_won(self):
        return self.val == self.WON
