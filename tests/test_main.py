from .context import Main


class NewGamePlay:
    def __init__(self):
        pass

    def next_step(self, resp):
        pass


def test_gameplay_prompt(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'user input')

    def prompt(self):
        self.prompt_called = True
        yield 'something'

    NewGamePlay.prompt = prompt
    new_game_play = NewGamePlay()

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert new_game_play.prompt_called


def test_gameplay_next_step(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: 'user input')

    def next_step(self, resp):
        self.resp = resp

    NewGamePlay.next_step = next_step
    new_game_play = NewGamePlay()

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert new_game_play.resp == 'user input'


def test_gameplay_loop(monkeypatch):
    monkeypatch.setitem(__builtins__, 'input', lambda x: x)

    def prompt(self):
        self.prompt_called = True
        yield 'something '
        yield 'something x2'

    def next_step(self, resp):
        self.resp += str(resp)

    NewGamePlay.prompt = prompt
    NewGamePlay.next_step = next_step

    new_game_play = NewGamePlay()
    new_game_play.resp = ''

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert new_game_play.resp == 'something ' + 'something x2'