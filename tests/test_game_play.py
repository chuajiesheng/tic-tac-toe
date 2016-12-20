from .context import GamePlay
import pytest


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


@pytest.fixture(scope='function')
def gameplay_in_play():
    g = GamePlay()
    g.players = ['one', 'two']
    g.state = 'PLAY'
    return g


def test_prompt_for_play(gameplay_in_play):
    assert gameplay_in_play.prompt() == '1 | 2 | 3\n' \
                                        '-----------\n' \
                                        '4 | 5 | 6\n' \
                                        '-----------\n' \
                                        "7 | 8 | 9\n\n" \
                                        "one, choose a box to place an 'x' into\n" \
                                        ">> "


def test_grid_with_one_answer(gameplay_in_play):
    gameplay_in_play.options[4] = 0
    assert gameplay_in_play.prompt() == '1 | 2 | 3\n' \
                                        '-----------\n' \
                                        '4 | x | 6\n' \
                                        '-----------\n' \
                                        "7 | 8 | 9\n\n" \
                                        "one, choose a box to place an 'x' into\n" \
                                        ">> "


def test_input_after_prompt(gameplay_in_play):
    gameplay_in_play.next_step('2')
    assert gameplay_in_play.options[1] == 0


def test_invalid_input_after_prompt(gameplay_in_play):
    current_player = gameplay_in_play.current_player

    gameplay_in_play.next_step('hello')
    assert gameplay_in_play.prompt().startswith('Please input a option from 1-9.')
    assert current_player == gameplay_in_play.current_player


def test_too_big_input_after_prompt(gameplay_in_play):
    current_player = gameplay_in_play.current_player

    gameplay_in_play.next_step('500')
    assert gameplay_in_play.prompt().startswith('Please input a option from 1-9.')
    assert current_player == gameplay_in_play.current_player


def test_handle_already_placed_box(gameplay_in_play):
    current_player = gameplay_in_play.current_player

    gameplay_in_play.options[4] = 0
    gameplay_in_play.next_step('5')
    assert gameplay_in_play.prompt().startswith('Option taken. Please choose another option.')
    assert current_player == gameplay_in_play.current_player


def test_change_player(gameplay_in_play):
    gameplay_in_play.next_step('5')
    assert gameplay_in_play.prompt() == '1 | 2 | 3\n' \
                                        '-----------\n' \
                                        '4 | x | 6\n' \
                                        '-----------\n' \
                                        "7 | 8 | 9\n\n" \
                                        "two, choose a box to place an 'o' into\n" \
                                        ">> "
