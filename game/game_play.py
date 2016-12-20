class GamePlay(object):
    DEFAULT_GRID = 3

    def __init__(self):
        self.state = 'NEW'
        self.players = []
        self.options = [None] * (self.DEFAULT_GRID * self.DEFAULT_GRID)

    def prompt(self):
        if self.state == 'NEW':
            no_of_players = len(self.players)
            if no_of_players < 2:
                return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)
        else:
            return self.get_grid(0)

    @staticmethod
    def box(xy, state):
        if state == 0:
            return 'x'
        elif state == 1:
            return 'o'

        return str(xy)

    def box_state(self, x, y):
        xy = (x * 3) + (y + 1)
        option = self.options[xy - 1]
        return self.box(xy, option)

    def row_state(self, x):
        row_elements = [self.box_state(x, y) for y in range(self.DEFAULT_GRID)]
        row_str = ' | '.join(row_elements)
        return row_str + '\n'

    def get_grid(self, player):
        grid_rows = [self.row_state(x) for x in range(self.DEFAULT_GRID)]
        len_of_row_divider = len(grid_rows[0]) + 1
        divider = ('-' * len_of_row_divider) + '\n'
        grid_str = divider.join(grid_rows)

        return "{}\n{}, choose a box to place an '{}' into\n >>".format(grid_str, self.players[player], self.box(0, player))

    def next_step(self, resp):
        self.players.append(resp)
        if len(self.players) >= 2:
            self.state = 'PLAY'

        return True

