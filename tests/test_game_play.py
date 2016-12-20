from .context import GamePlay


def test_prompt():
    g = GamePlay()
    first_prompt = g.prompt()
    assert first_prompt == 'Enter name for Player 1:\n>> '


def test_save_player():
    g = GamePlay()
    new_player = 'Player X'
    g.next_step(new_player)
    assert len(g.players) == 1
    assert g.players[0] == new_player


def test_need_two_player():
    g = GamePlay()
    g.players = ['one']
    next_prompt = g.prompt()
    assert next_prompt == 'Enter name for Player 2:\n>> '


def test_print_change_state():
    g = GamePlay()
    g.players = ['one']
    assert g.next_step('two')
    assert g.state == 'PLAY'


def test_prompt_for_play():
    g = GamePlay()
    g.players = ['one', 'two']
    g.state = 'PLAY'
    assert g.prompt() == '1 | 2 | 3\n' \
                         '-----------\n' \
                         '4 | 5 | 6\n' \
                         '-----------\n' \
                         "7 | 8 | 9\n\n" \
                         "one, choose a box to place an 'x' into"
