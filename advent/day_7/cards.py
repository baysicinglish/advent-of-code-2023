from __future__ import annotations

from typing import Sequence, Tuple
from functools import total_ordering, cached_property
from enum import Enum


class HouseRules(Enum):
    JOKER = "Joker ruling"


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

    def __init__(self, cards: Sequence[Card], house_rules: Tuple[HouseRules | None] = tuple()):
        assert len(cards) == 5, "A hand is comprised of 5 cards"
        self.cards = cards
        self.house_rules = house_rules

    def __repr__(self):
        return f"Hand[{''.join(card.value for card in self.cards)}]"

    def __lt__(self, other: Hand):
        if self.type == other.type:
            for index, current_card in enumerate(self.cards):
                if current_card == other.cards[index]:
                    continue

                if HouseRules.JOKER in self.house_rules:
                    if current_card.value == "J" or other.cards[index].value == "J":
                        return current_card.value == "J"

                return current_card < other.cards[index]

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

        if HouseRules.JOKER in self.house_rules:
            joker_count = card_counts.pop("J", 0)
            if not card_counts:
                return self.Types.FIVE_OF_A_KIND
            largest_count = max(card_counts, key=card_counts.get)
            card_counts[largest_count] += joker_count

        card_counts = tuple(card_counts.values())

        if 5 in card_counts:
            return self.Types.FIVE_OF_A_KIND

        if 4 in card_counts:
            return self.Types.FOUR_OF_A_KIND

        if 3 in card_counts:
            return self.Types.FULL_HOUSE if 2 in card_counts else self.Types.THREE_OF_A_KIND

        if 2 in card_counts:
            return self.Types.TWO_PAIR if card_counts.count(2) == 2 else self.Types.PAIR

        return self.Types.HIGH_CARD
