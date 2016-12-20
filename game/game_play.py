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

    def prompt(self):
        if self.state == 'NEW':
            no_of_players = len(self.players)
            if no_of_players < 2:
                return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)
        else:
            return self.error + self.get_grid(0)

    def get_grid(self, player):
        def x_or_o(xy, state):
            return str(xy) if state is None else self.PLAYER_SHAPE[state]

        def box_state(x, y):
            xy = (x * 3) + y
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
        player_name = self.players[player]

        return self.CHOICE_PROMPT.format(grid_str, player_name, self.PLAYER_SHAPE[player])

    def next_step(self, resp):
        def handle_player_name(resp):
            self.players.append(resp)
            if len(self.players) >= 2:
                self.state = 'PLAY'

        def handle_options(resp):
            option = resp.isdigit() and int(resp)
            within_limits = option and 0 <= option <= (self.DEFAULT_GRID * self.DEFAULT_GRID)
            already_taken = not within_limits or self.options[option - 1] is not None

            if not within_limits:
                self.error = self.INVALID_OPTION.format(self.DEFAULT_GRID * self.DEFAULT_GRID)
            elif already_taken:
                self.error = self.OPTION_TAKEN
            else:
                self.options[option - 1] = 0

        if self.state == 'NEW':
            handle_player_name(resp)
        else:
            handle_options(resp)

        return True

