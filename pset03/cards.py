from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal_game(number_of_hands, cards_per_hand):
   if not isinstance(number_of_hands, int) or isinstance(number_of_hands, bool):
        raise TypeError("number_of_hands must be an integer")

    if not isinstance(cards_per_hand, int) or isinstance(cards_per_hand, bool):
        raise TypeError("cards_per_hand must be an integer")

    if number_of_hands < 1 or cards_per_hand < 1:
        raise ValueError("Both numbers must be positive")

    if number_of_hands * cards_per_hand > 52:
        raise ValueError("Not enough cards in the deck")

    deck = shuffled_deck()
    hands = []

    for i in range(number_of_hands):
        start = i * cards_per_hand
        end = start + cards_per_hand
        hand = set(deck[start:end])
        hands.append(hand)

    return hands


def poker_classn(hand):
    if not isinstance(hand, set):
        raise TypeError("hand must be a set")

    if len(hand) != 5:
        raise ValueError("hand must contain exactly 5 cards")

    for card in hand:
        if not isinstance(card, Card):
            raise TypeError("hand must contain Card objects")

    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]

    rank_counts = {}

    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    counts = sorted(rank_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1

    sorted_ranks = sorted(ranks)

    is_straight = (
        len(set(ranks)) == 5 and
        sorted_ranks[-1] - sorted_ranks[0] == 4
    )

    if set(ranks) == {1, 2, 3, 4, 5}:
        is_straight = True

    if is_flush and set(ranks) == {1, 10, 11, 12, 13}:
        return "Royal Flush"

    if is_straight and is_flush:
        return "Straight Flush"

    if counts == [4, 1]:
        return "Four of a Kind"

    if counts == [3, 2]:
        return "Full House"

    if is_flush:
        return "Flush"

    if is_straight:
        return "Straight"

    if counts == [3, 1, 1]:
        return "Three of a Kind"

    if counts == [2, 2, 1]:
        return "Two Pair"

    if counts == [2, 1, 1, 1]:
        return "One Pair"

    return "High Card"

