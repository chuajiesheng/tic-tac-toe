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
        return 'something'

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
        return 'something'

    def next_step(self, resp):
        self.players.append(resp)
        if len(self.players) >= 2:
            return False

        return True

    NewGamePlay.prompt = prompt
    NewGamePlay.next_step = next_step

    new_game_play = NewGamePlay()
    new_game_play.players = []

    m = Main()
    m.game_play = new_game_play

    m.start()
    assert len(new_game_play.players) == 2