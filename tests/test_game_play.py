from .context import GamePlay


class TestGamePlay:
    def test_prompt(self):
        g = GamePlay()
        assert g.prompt() == 'Enter name for Player 1:\n>> '