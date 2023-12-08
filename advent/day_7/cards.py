from __future__ import annotations

from typing import Sequence
from functools import total_ordering, cached_property
from enum import Enum


@total_ordering
class Card:
    VALUES = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

    def __init__(self, value):
        assert str(value) in self.VALUES, f"Card value '{value}' not a valid card value '{self.VALUES}'"
        self.value = value

    def __repr__(self):
        return f"Card[{self.value}]"

    def __eq__(self, other: Card):
        return self.value == other.value

    def __gt__(self, other: Card):
        return self.VALUES.index(self.value) < self.VALUES.index(other.value)


class Hand:
    class Types(Enum):
        FIVE_OF_A_KIND = "Five of a kind"
        FOUR_OF_A_KIND = "Four of a kind"
        FULL_HOUSE = "Full house"
        THREE_OF_A_KIND = "Three of a kind"
        TWO_PAIR = "Two pair"
        PAIR = "Pair"
        HIGH_CARD = "High card"

    def __init__(self, cards: Sequence[Card]):
        assert len(cards) == 5, "A hand is comprised of 5 cards"
        self.cards = cards

    def __repr__(self):
        return f"Hand[{''.join(card.value for card in self.cards)}]"

    def __lt__(self, other: Hand):
        if self.type == other.type:
            for index, value in enumerate(self.cards):
                if value == other.cards[index]:
                    continue
                return value < other.cards[index]

        for hand_type in self.Types:
            if other.type == hand_type:
                return True
            if self.type == hand_type:
                return False

    @cached_property
    def type(self):
        card_counts = {}
        for card in self.cards:
            card_counts[card.value] = card_counts.get(card.value, 0) + 1
        card_counts = list(card_counts.values())

        if 5 in card_counts:
            return self.Types.FIVE_OF_A_KIND

        if 4 in card_counts:
            return self.Types.FOUR_OF_A_KIND

        if 3 in card_counts:
            return self.Types.FULL_HOUSE if 2 in card_counts else self.Types.THREE_OF_A_KIND

        if 2 in card_counts:
            return self.Types.TWO_PAIR if card_counts.count(2) == 2 else self.Types.PAIR

        return self.Types.HIGH_CARD
