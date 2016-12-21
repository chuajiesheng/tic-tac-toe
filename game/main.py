from game import GamePlay
import sys

class Main:
    def __init__(self, size=3):
        self.game_play = GamePlay(size)

    def start(self):
        while True:
            resp = input(self.game_play.prompt())
            has_next = self.game_play.next_step(resp)
            if not has_next:
                print(self.game_play.prompt())
                break


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        d = args[1].isdigit() and int(args[1])

    m = Main(d)
    m.start()