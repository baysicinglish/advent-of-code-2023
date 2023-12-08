import pytest

from .cards import Card, Hand, HouseRules


class TestCard:
    def test_card_equality(self):
        for current_value in Card.VALUES:

            other_values = [value for value in Card.VALUES if value != current_value]
            card = Card(current_value)

            assert (card == Card(current_value)) is True
            for comparison_value in other_values:
                assert (card == Card(comparison_value)) is False

    def test_card_comparison(self):
        card = Card("J")

        for value in Card.VALUES:
            comparison_card = Card(value)
            expected_result = True if value in ("A", "K", "Q") else False
            assert (card < comparison_card) is expected_result


class TestHand:
    @pytest.mark.parametrize("cards, hand_type", [
        ("32T3K", Hand.Types.PAIR),
        ("T55J5", Hand.Types.THREE_OF_A_KIND),
        ("KK677", Hand.Types.TWO_PAIR),
        ("KTJJT", Hand.Types.TWO_PAIR),
        ("QQQJA", Hand.Types.THREE_OF_A_KIND),
    ])
    def test_hand_type(self, cards, hand_type):
        cards = [Card(card) for card in cards]
        hand = Hand(cards)

        assert hand.type == hand_type

    @pytest.mark.parametrize("cards, hand_type", [
        ("KTJJT", Hand.Types.FOUR_OF_A_KIND),
        ("JJJJJ", Hand.Types.FIVE_OF_A_KIND)
    ])
    def test_hand_type_with_joker_rule(self, cards, hand_type):
        cards = [Card(card) for card in cards]
        hand = Hand(cards, house_rules=(HouseRules.JOKER,))

        assert hand.type == hand_type

    @pytest.mark.parametrize("lower_hand, upper_hand", [
        ("32T3K", "KTJJT"),
        ("KTJJT", "KK677"),
        ("KTJJT", "T55J5"),
        ("T55J5", "QQQJA")
    ])
    def test_hand_comparison(self, lower_hand, upper_hand):
        lower_hand = Hand([Card(card) for card in lower_hand])
        upper_hand = Hand([Card(card) for card in upper_hand])

        assert lower_hand < upper_hand

    def test_hand_comparison_with_joker_rule(self):
        lower_hand = Hand([Card(card) for card in "JKKK2"])
        upper_hand = Hand([Card(card) for card in "QQQQ2"])

        assert lower_hand < upper_hand
