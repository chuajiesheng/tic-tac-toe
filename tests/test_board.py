from .context import Board
import pytest


def test_grid():
    b = Board()
    assert b.get_grid() == '1 | 2 | 3\n' \
                           '-----------\n' \
                           '4 | 5 | 6\n' \
                           '-----------\n' \
                           "7 | 8 | 9\n"


def test_grid_with_one_answer():
    b = Board()
    b.options[4] = 0
    assert b.get_grid() == '1 | 2 | 3\n' \
                           '-----------\n' \
                           '4 | x | 6\n' \
                           '-----------\n' \
                           "7 | 8 | 9\n"


def test_horizontal_winning_combi():
    b = Board()
    b.options[0] = 0
    b.options[1] = 0
    b.options[2] = 0
    assert b.player_won(0)


def test_horizontal_winning_combi_2():
    b = Board()
    b.options[3] = 0
    b.options[4] = 0
    b.options[5] = 0
    assert b.player_won(0)


def test_horizontal_winning_combi_3():
    b = Board()
    b.options[6] = 0
    b.options[7] = 0
    b.options[8] = 0
    assert b.player_won(0)


def test_vertical_winning_combi():
    b = Board()
    b.options[0] = 0
    b.options[3] = 0
    b.options[6] = 0
    assert b.player_won(0)


def test_vertical_winning_combi_2():
    b = Board()
    b.options[1] = 0
    b.options[4] = 0
    b.options[7] = 0
    assert b.player_won(0)


def test_vertical_winning_combi_3():
    b = Board()
    b.options[2] = 0
    b.options[5] = 0
    b.options[8] = 0
    assert b.player_won(0)


def test_diagonal_winning_combi():
    b = Board()
    b.options[0] = 0
    b.options[4] = 0
    b.options[8] = 0
    assert b.player_won(0)


def test_diagonal_winning_combi_2():
    b = Board()
    b.options[2] = 0
    b.options[4] = 0
    b.options[6] = 0
    assert b.player_won(0)


def test_max_option():
    b = Board()
    assert b.max_option() == 9


def test_no_option_left():
    b = Board()
    b.options = [0] * 9
    assert b.have_no_more_option()


def test_no_option_left():
    b = Board()
    b.options = [0] * 9
    b.options[8] = None
    assert b.have_no_more_option() is not True


def test_option_unavailable():
    b = Board()
    b.options[0] = 0
    assert b.option_unavailable(0)


def test_option_available():
    b = Board()
    assert b.option_unavailable(0) is not True


def test_set_option():
    b = Board()
    b.set_option(0, 1)
    assert b.options[0] == 1
