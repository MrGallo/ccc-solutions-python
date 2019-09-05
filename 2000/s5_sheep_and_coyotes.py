def mock_input():
    value = mock_input.inputs[mock_input.i]
    mock_input.i += 1
    return value
mock_input.i = 0
mock_input.inputs = """6
100.00
100.00
200.00
150.00
140.00
200.00
100.00
300.00
300.00
300.00
300.00
100.00""".split("\n")
input = mock_input

from collections import defaultdict


def distance_squared(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

num_sheep = int(input())

sheep_locations = []
for _ in range(num_sheep):
    x = float(input())
    y = float(input())
    sheep_locations.append((x, y))

potential_eaten_sheep = set()
coyote_y = 0
for coyote_x in range(1000):  # range(1001)???
    distance_sheep = defaultdict(list)
    for i, (sheep_x, sheep_y) in enumerate(sheep_locations):
        distance = distance_squared(coyote_x, coyote_y, sheep_x, sheep_y)
        distance_sheep[distance].append((sheep_x, sheep_y))
    shortest_distance = min(distance_sheep.keys())
    for sheep_location in distance_sheep[shortest_distance]:
        potential_eaten_sheep.add(sheep_location)

for x, y in potential_eaten_sheep:
    print("The sheep at ({:0.2f}, {:0.2f}) might be eaten.".format(x, y))
