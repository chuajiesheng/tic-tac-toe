from .context import Main


class NewGamePlay:
    def __init__(self):
        self.prompt_called = False
        self.next_step_called = False
        self.next_step_called_with = None

    def prompt(self):
        self.prompt_called = True
        yield 'something'

    def next_step(self, something):
        self.next_step_called = True
        self.next_step_called_with = something


def test_gameplay_prompt(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'user input')

    new_game_play = NewGamePlay()

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert new_game_play.prompt_called


def test_gameplay_next_step(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'user input')

    new_game_play = NewGamePlay()

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert new_game_play.next_step_called
    assert new_game_play.next_step_called_with == 'user input'


