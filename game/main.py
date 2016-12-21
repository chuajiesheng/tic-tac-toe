from game import GamePlay
from game import Board
import sys


class Main:
    def __init__(self, size):
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

    d = None
    if len(args) > 1:
        d = args[1].isdigit() and int(args[1])

    m = Main(d or Board.DEFAULT_GRID)
    m.start()