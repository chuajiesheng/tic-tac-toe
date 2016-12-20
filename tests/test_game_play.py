from .context import GamePlay


class TestGamePlay:
    def test_prompt(self):
        g = GamePlay()
        first_prompt = list(g.prompt())[0]
        assert first_prompt == 'Enter name for Player 1:\n>> '

    def test_save_player(self):
        g = GamePlay()
        new_player = 'Player X'
        g.next_step(new_player)
        assert len(g.players) == 1
        assert g.players[0] == new_player