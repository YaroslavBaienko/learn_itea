import random

from poker import *

if __name__ == '__main__':
    deck = list(Card)
    random.shuffle(deck)
    flop = [deck.pop() for _ in range(3)]
    turn = deck.pop()
    river = deck.pop()
    print(flop, turn, river)
