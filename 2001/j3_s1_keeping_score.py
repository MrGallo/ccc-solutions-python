
CARD_POINT_VALUES = {
    "A": 4,
    "K": 3,
    "Q": 2,
    "J": 1
}

SUIT_POINT_VALUES = {
    0: 3,
    1: 2,
    2: 1
}


hand_str = input()

hand = {
    "clubs": [],
    "diamonds": [],
    "hearts": [],
    "spades": []
}

current_suit = None

for char in hand_str:
    if char == "C":
        current_suit = "clubs"
    elif char == "D":
        current_suit = "diamonds"
    elif char == "H":
        current_suit = "hearts"
    elif char == "S":
        current_suit = "spades"
    else:
        hand[current_suit].append(char)


total_points = 0
print("Cards Dealt              Points")
for suit in sorted(hand.keys()):
    suit_points = 0
    for card in hand[suit]:
        if card in CARD_POINT_VALUES.keys():
            suit_points += CARD_POINT_VALUES[card]
    
    if len(hand[suit]) in SUIT_POINT_VALUES.keys():
        suit_points += SUIT_POINT_VALUES[len(hand[suit])]
    
    total_points += suit_points

    name_and_cards = "{} {}".format(suit.capitalize(), " ".join(hand[suit]))
    print("{:<29} {}".format(name_and_cards, suit_points))

print("Total {}".format(total_points).rjust(31))