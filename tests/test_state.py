from .context import State


def test_new():
    s = State()
    assert s.is_new()


def test_move():
    s = State()
    s.move()
    assert s.is_play()


def test_move_2():
    s = State()
    s.move()
    s.move()
    assert s.is_won()



