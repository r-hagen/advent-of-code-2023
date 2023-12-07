lines = [line.strip() for line in open("in").readlines()]


def part1(lines):
    def card_strength(card):
        cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return len(cards) - cards.index(card)

    def hand_strength(hand):
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        if 5 in counts.values():
            return 6
        elif 4 in counts.values():
            return 5
        elif 3 in counts.values() and 2 in counts.values():
            return 4
        elif 3 in counts.values():
            return 3
        elif len([x for x in counts.values() if x == 2]) == 2:
            return 2
        elif 2 in counts.values():
            return 1
        return 0

    ranked = []
    for line in lines:
        hand, bid = line.split()
        strength_hand = hand_strength(hand)
        strength_cards = tuple([card_strength(card) for card in hand])
        ranked.append((strength_hand, strength_cards, hand, int(bid)))

    ranked = sorted(ranked)

    total = 0
    for rank, (_, _, _, bid) in enumerate(ranked, 1):
        total += rank * bid
    return total


def part2(lines):
    def card_strength(card):
        cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        return len(cards) - cards.index(card)

    def hand_strength(hand):
        js = 0
        counts = {}
        for card in hand:
            if card == "J":
                js += 1
            else:
                counts[card] = counts.get(card, 0) + 1
        # five of a kind
        if js == 5:
            return 6
        elif 5 in counts.values():
            return 6
        elif js + max(counts.values()) == 5:
            return 6
        # four of a kind
        elif js == 4:
            return 5
        elif 4 in counts.values():
            return 5
        elif js + max(counts.values()) == 4:
            return 5
        # full  house
        elif js == 3 and 2 in counts.values():
            return 4
        elif 3 in counts.values() and js == 2:
            return 4
        elif 3 in counts.values() and 2 in counts.values():
            return 4
        elif 3 in counts.values() and 1 in counts.values() and js == 1:
            return 4
        elif len([x for x in counts.values() if x == 2]) == 2 and js == 1:
            return 4
        # three of a kind
        elif js == 3:
            return 3
        elif 3 in counts.values():
            return 3
        elif js + max(counts.values()) == 3:
            return 3
        # two pairs
        elif js == 2 and 2 in counts.values():
            return 2
        elif len([x for x in counts.values() if x == 2]) == 2:
            return 2
        elif 2 in counts.values() and 1 in counts.values() and js == 1:
            return 2
        # one pair
        elif js == 1 and 1 in counts.values():
            return 1
        elif 2 in counts.values():
            return 1
        return 0

    ranked = []
    for line in lines:
        hand, bid = line.split()
        strength_hand = hand_strength(hand)
        strength_cards = tuple([card_strength(card) for card in hand])
        ranked.append((strength_hand, strength_cards, hand, int(bid)))

    ranked = sorted(ranked)

    total = 0
    for rank, (_, _, _, bid) in enumerate(ranked, 1):
        total += rank * bid
    return total


print("part1", part1(lines))
print("part2", part2(lines))
