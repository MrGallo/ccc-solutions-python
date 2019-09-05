
""" Advanced solution:

POINT_VALUES = [3, 2, 1]

inputs = [int(input()) for _ in range(6)]

team_a_score = sum([baskets_made * point_value for baskets_made, point_value in zip(inputs[0:3], POINT_VALUES)])
team_b_score = sum([baskets_made * point_value for baskets_made, point_value in zip(inputs[3:], POINT_VALUES)])

if team_a_score > team_b_score:
    print("A")
elif team_b_score > team_a_score:
    print("B")
else:
    print("T")
"""


a_threes = int(input()) * 3
a_twos = int(input()) * 2
a_ones = int(input())

b_threes = int(input()) * 3
b_twos = int(input()) * 2
b_ones = int(input())

team_a_score = a_threes + a_twos + a_ones
team_b_score = b_threes + b_twos + b_ones

if team_a_score > team_b_score:
    print("A")
elif team_b_score > team_a_score:
    print("B")
else:
    print("T")


