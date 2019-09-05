# CCC 2001 Solution Summary

## Junior 1 - Dressing Up
```python
import math


rows = int(input())

for row in range(1, rows, 2):
    print("*" * row, "*" * row, sep=" " * (rows*2-row*2))

for row in range(rows, 0, -2):
    print("*" * row, "*" * row, sep=" " * (rows*2-row*2))
```

### Topics
- String multiplication
- String concatenation
- `print` and `sep`
- Looping over a range

## Junior 2 - Mod Inverse
```python
x = int(input())
m = int(input())

for n in range(m):
    if x * n % m == 1:
        print(n)
        break
else:
    print("No such integer exists.")
```

### Topics
- If statements
- Loops
  - `break`
  - `else` or "No-Break"

## Junior 3/Senior 1 - Keeping Score
```python

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
```