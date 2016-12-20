from game import GamePlay


class Main:
    def __init__(self):
        self.game_play = GamePlay()

    def start(self):
        for prompt in self.game_play.prompt():
            resp = input(prompt)
            self.game_play.next_step(resp)


if __name__ == '__main__':
    m = Main()
    m.start()