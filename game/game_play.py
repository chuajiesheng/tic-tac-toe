class GamePlay(object):
    def __init__(self):
        self.state = 'NEW'
        self.players = []

    def prompt(self):
        no_of_players = len(self.players)
        if no_of_players < 2:
            return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)

    def next_step(self, resp):
        self.players.append(resp)
        if len(self.players) >= 2:
            return False

        return True

