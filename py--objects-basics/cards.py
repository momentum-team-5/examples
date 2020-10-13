import random


class CardError(Exception):
    pass


def get_pretty_rank(rank):
    if rank < 11:
        return rank

    elif rank == 11:
        return "J"

    elif rank == 12:
        return "Q"

    elif rank == 13:
        return "K"

    elif rank == 14:
        return "A"



def get_pretty_suit(suit):
    if suit == "spades":
        return chr(0x2660)

    elif suit == "clubs":
        return chr(0x2663)

    elif suit == "hearts":
        return chr(0x2665)

    else:
        return chr(0x2666)


class Card:
    SUITS = {"spades", "clubs", "diamonds", "hearts"}
    RANKS = set(range(2, 15))

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError(f"{suit} is not a valid suit.")

        if rank not in self.RANKS:
            raise ValueError(f"{rank} is not a valid rank.")

        self.suit = suit
        self.rank = rank

    def samesuit(self, other):
        return self.suit == other.suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __str__(self):
        pretty_suit = get_pretty_suit(self.suit)
        pretty_rank = get_pretty_rank(self.rank)
        return f"{pretty_rank}-{pretty_suit}"
    

class Deck:
    def __init__(self):
        self.cards = []

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    pass
