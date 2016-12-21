class Board(object):
    DEFAULT_GRID = 3
    PLAYER_SHAPE = {
        0: 'x',
        1: 'o'
    }

    def __init__(self, size):
        self.grid = size
        self.options = [None] * (self.grid * self.grid)

    def get_grid(self):
        def x_or_o(xy, state):
            return str(xy) if state is None else self.PLAYER_SHAPE[state]

        def box_state(x, y):
            xy = (x * self.grid) + y
            option = self.options[xy]
            return x_or_o(xy + 1, option)

        def row_state(x):
            row_elements = [box_state(x, y) for y in range(self.grid)]
            row_str = ' | '.join(row_elements)
            return row_str + '\n'

        def divider(length):
            return ('-' * length) + '\n'

        grid_rows = [row_state(x) for x in range(self.grid)]
        return divider(len(grid_rows[0]) + 1).join(grid_rows)

    def player_won(self, current_player):
        def owned_by_current_player(x, y):
            return self.options[(x * self.grid) + y] == current_player

        def check_row(x):
            return all([owned_by_current_player(x, y) for y in range(self.grid)])

        def check_col(x):
            return all([owned_by_current_player(y, x) for y in range(self.grid)])

        horizontal = any([check_row(x) for x in range(self.grid)])
        vertical = any([check_col(col) for col in range(self.grid)])
        forward_diagonal = all([owned_by_current_player(x, x) for x in range(self.grid)])
        backward_diagonal = all([owned_by_current_player(x, self.grid - x - 1) for x in range(self.grid)])

        return any([horizontal, vertical, forward_diagonal, backward_diagonal])

    def max_option(self):
        return self.grid * self.grid

    def have_no_more_option(self):
        return len([x for x in self.options if x is None]) < 1

    def option_unavailable(self, option):
        return self.options[option] is not None

    def set_option(self, option, player):
        self.options[option] = player
        return True