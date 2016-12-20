class GamePlay(object):
    def __init__(self):
        self.state = 'NEW'
        self.players = []

    def prompt(self):
        if self.state == 'NEW':
            no_of_players = len(self.players)
            if no_of_players < 2:
                return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)
        else:
            return '1 | 2 | 3\n' \
                         '-----------\n' \
                         '4 | 5 | 6\n' \
                         '-----------\n' \
                         "7 | 8 | 9\n\n" \
                         "{}, choose a box to place an 'x' into".format(self.players[0])

    def next_step(self, resp):
        self.players.append(resp)
        if len(self.players) >= 2:
            self.state = 'PLAY'

        return True

