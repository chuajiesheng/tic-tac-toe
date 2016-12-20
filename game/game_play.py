class GamePlay(object):
    def __init__(self):
        self.state = 'NEW'
        self.players = []

    def prompt(self):
        yield 'Enter name for Player 1:\n>> '

    def next_step(self, resp):
        self.players.append(resp)

