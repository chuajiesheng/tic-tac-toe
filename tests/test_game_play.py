from .context import GamePlay


def test_prompt():
    g = GamePlay()
    first_prompt = list(g.prompt())[0]
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
    next_prompt = list(g.prompt())[0]
    assert next_prompt == 'Enter name for Player 2:\n>> '
