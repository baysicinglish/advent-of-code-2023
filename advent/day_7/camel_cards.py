from typing import List, Tuple

from .cards import Hand, Card


def parse_camel_card_bids(bids_file) -> List[Tuple[Hand, int]]:
    parsed_bids = []

    with open(f"day_7/inputs/{bids_file}", "r") as bids:
        for bid in bids:
            hand, bid_amount = bid.split()
            cards = [Card(card) for card in hand]
            parsed_bids.append((Hand(cards), int(bid_amount)))

    return parsed_bids


if __name__ == "__main__":
    bids = parse_camel_card_bids("challenge.txt")
    bids.sort()

    total_winnings = 0
    for rank, bid in enumerate([bid for hand, bid in bids], 1):
        total_winnings += rank * bid

    print(total_winnings)
