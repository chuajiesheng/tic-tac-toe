class GamePlay(object):
    DEFAULT_GRID = 3
    CHOICE_PROMPT = "{}\n{}, choose a box to place an '{}' into\n>> "
    PLAYER_SHAPE = {
        0: 'x',
        1: 'o'
    }
    INVALID_OPTION = 'Please input a option from 1-{}.\n\n'
    OPTION_TAKEN = 'Option taken. Please choose another option.\n\n'

    def __init__(self):
        self.state = 'NEW'
        self.players = []
        self.options = [None] * (self.DEFAULT_GRID * self.DEFAULT_GRID)
        self.error = ''
        self.current_player = 0

    def prompt(self):
        def get_error():
            current_error = self.error
            self.error = ''
            return current_error

        if self.state == 'NEW':
            no_of_players = len(self.players)
            if no_of_players < 2:
                return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)
        else:
            return get_error() + self.get_grid(self.current_player)

    def get_grid(self, next_player):
        def x_or_o(xy, state):
            return str(xy) if state is None else self.PLAYER_SHAPE[state]

        def box_state(x, y):
            xy = (x * self.DEFAULT_GRID) + y
            option = self.options[xy]
            return x_or_o(xy + 1, option)

        def row_state(x):
            row_elements = [box_state(x, y) for y in range(self.DEFAULT_GRID)]
            row_str = ' | '.join(row_elements)
            return row_str + '\n'

        def divider(length):
            return ('-' * length) + '\n'

        grid_rows = [row_state(x) for x in range(self.DEFAULT_GRID)]
        grid_str = divider(len(grid_rows[0]) + 1).join(grid_rows)
        print(next_player)
        player_name = self.players[next_player]

        return self.CHOICE_PROMPT.format(grid_str, player_name, self.PLAYER_SHAPE[next_player])

    def check_win(self):
        def owned_by_current_player(x, y):
            return self.options[(x * self.DEFAULT_GRID) + y] == self.current_player

        def check_row(x):
            return all([owned_by_current_player(x, y) for y in range(self.DEFAULT_GRID)])

        def check_col(x):
            return all([owned_by_current_player(y, x) for y in range(self.DEFAULT_GRID)])

        horizontal = any([check_row(x) for x in range(self.DEFAULT_GRID)])
        vertical = any([check_col(col) for col in range(self.DEFAULT_GRID)])
        forward_diagonal = all([owned_by_current_player(x, x) for x in range(self.DEFAULT_GRID)])
        backward_diagonal = all([owned_by_current_player(x, self.DEFAULT_GRID - x - 1) for x in range(self.DEFAULT_GRID)])

        return any([horizontal, vertical, forward_diagonal, backward_diagonal])

    def next_step(self, resp):
        def handle_player_name(resp):
            self.players.append(resp)
            if len(self.players) >= 2:
                self.state = 'PLAY'

        def next_player():
            self.current_player = 1 if self.current_player == 0 else 0

        def handle_options(resp):
            option = resp.isdigit() and int(resp)
            within_limits = option and 0 <= option <= (self.DEFAULT_GRID * self.DEFAULT_GRID)

            if not within_limits:
                self.error = self.INVALID_OPTION.format(self.DEFAULT_GRID * self.DEFAULT_GRID)
            elif self.options[option - 1] is not None:
                self.error = self.OPTION_TAKEN
            else:
                self.options[option - 1] = self.current_player
                self.check_win()
                next_player()

        if self.state == 'NEW':
            handle_player_name(resp)
        else:
            handle_options(resp)

        return True

