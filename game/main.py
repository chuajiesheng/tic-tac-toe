from game import GamePlay


class Main:
    def __init__(self):
        self.game_play = GamePlay()

    def start(self):
        while True:
            resp = input(self.game_play.prompt())
            has_next = self.game_play.next_step(resp)
            if not has_next:
                print(self.game_play.prompt())
                break


if __name__ == '__main__':
    m = Main()
    m.start()