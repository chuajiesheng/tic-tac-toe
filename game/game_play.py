from game import State


class Board(object):
    DEFAULT_GRID = 3
    PLAYER_SHAPE = {
        0: 'x',
        1: 'o'
    }

    def __init__(self):
        self.options = [None] * (self.DEFAULT_GRID * self.DEFAULT_GRID)

    def get_grid(self):
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
        return divider(len(grid_rows[0]) + 1).join(grid_rows)

    def player_won(self, current_player):
        def owned_by_current_player(x, y):
            return self.options[(x * self.DEFAULT_GRID) + y] == current_player

        def check_row(x):
            return all([owned_by_current_player(x, y) for y in range(self.DEFAULT_GRID)])

        def check_col(x):
            return all([owned_by_current_player(y, x) for y in range(self.DEFAULT_GRID)])

        horizontal = any([check_row(x) for x in range(self.DEFAULT_GRID)])
        vertical = any([check_col(col) for col in range(self.DEFAULT_GRID)])
        forward_diagonal = all([owned_by_current_player(x, x) for x in range(self.DEFAULT_GRID)])
        backward_diagonal = all([owned_by_current_player(x, self.DEFAULT_GRID - x - 1) for x in range(self.DEFAULT_GRID)])

        return any([horizontal, vertical, forward_diagonal, backward_diagonal])

    def max_option(self):
        return self.DEFAULT_GRID * self.DEFAULT_GRID

    def have_no_more_option(self):
        return len([x for x in self.options if x is None]) < 1

    def option_available(self, option):
        return self.options[option] is not None

    def set_option(self, option, player):
        self.options[option] = player
        return True


class GamePlay(object):

    CHOICE_PROMPT = "{}\n{}, choose a box to place an '{}' into\n>> "
    INVALID_OPTION = 'Please input a option from 1-{}.\n\n'
    OPTION_TAKEN = 'Option taken. Please choose another option.\n\n'

    def __init__(self):
        self.state = State()
        self.board = Board()
        self.players = []
        self.banner = ''
        self.current_player = 0

    def prompt(self):
        def get_banner():
            banner = self.banner
            self.banner = ''
            return banner

        def get_prompt(next_player):
            player_name = self.players[next_player]
            grid = self.board.get_grid()
            return self.CHOICE_PROMPT.format(grid, player_name, self.board.PLAYER_SHAPE[next_player])

        if self.state.is_new():
            no_of_players = len(self.players)
            if no_of_players < 2:
                return 'Enter name for Player {}:\n>> '.format(no_of_players + 1)
        elif self.state.is_play():
            return get_banner() + get_prompt(self.current_player)
        else:
            return get_banner()

    def next_step(self, resp):
        def handle_player_name(resp):
            self.players.append(resp)
            if len(self.players) >= 2:
                self.state.move()

        def next_player():
            self.current_player = 1 if self.current_player == 0 else 0

        def win():
            self.state.move()
            self.banner = 'Congratulations {}! You have won.'.format(self.players[self.current_player])
            return True

        def no_more_option_left():
            no_more_option = self.board.have_no_more_option()
            if no_more_option:
                self.state.move()
                self.banner = 'Game ended. No one won.'.format(self.players[self.current_player])

            return no_more_option

        def handle_options(resp):
            option = resp.isdigit() and int(resp)
            within_limits = option and 0 <= option <= self.board.max_option()

            if not within_limits:
                self.banner = self.INVALID_OPTION.format(self.board.max_option())
            elif self.board.option_available(option - 1):
                self.banner = self.OPTION_TAKEN
            else:
                self.board.set_option(option - 1, self.current_player)
                game_finished = self.board.player_won(self.current_player) and win()
                game_finished or no_more_option_left() or next_player()

        if self.state.is_new():
            handle_player_name(resp)
        else:
            handle_options(resp)

        return not self.state.is_won()

