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

    def get_grid(self, player):
        def x_or_o(xy, state):
            return str(xy) if state is None else ('x' if state == 0 else 'o')

        def box_state(x, y):
            xy = (x * 3) + (y + 1)
            option = self.options[xy - 1]
            return x_or_o(xy, option)

        def row_state(x):
            row_elements = [box_state(x, y) for y in range(self.DEFAULT_GRID)]
            row_str = ' | '.join(row_elements)
            return row_str + '\n'

        def divider(length):
            return ('-' * length) + '\n'

        grid_rows = [row_state(x) for x in range(self.DEFAULT_GRID)]
        grid_str = divider(len(grid_rows[0]) + 1).join(grid_rows)

        return "{}\n{}, choose a box to place an '{}' into\n >>".format(grid_str, self.players[player], x_or_o(0, player))

    def next_step(self, resp):
        self.players.append(resp)
        if len(self.players) >= 2:
            self.state = 'PLAY'

        return True

