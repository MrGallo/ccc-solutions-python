def mock_input():
    inputs = """100
3
33
66
1""".split("\n")
    value = inputs[mock_input.i]
    mock_input.i += 1
    return value
mock_input.i = 0
input = mock_input


def get_lowest_strokes(distance, club_distances, distance_memo=None):
    if distance == 0:
        return 0

    if distance_memo is None:
        distance_memo = {}

    if distance in distance_memo.keys():
        return distance_memo[distance]

    lowest_strokes = None
    for club in club_distances:
        if distance >= club:
            distance_after_stroke = distance - club
            result = get_lowest_strokes(distance_after_stroke, club_distances, distance_memo)
            if result is None:
                continue
            strokes = 1 + result
            if lowest_strokes is None or result < lowest_strokes:
                lowest_strokes = strokes

    distance_memo[distance] = lowest_strokes
    return lowest_strokes


distance = int(input())
num_clubs = int(input())


club_distances = []
for _ in range(num_clubs):
    club_distances.append(int(input()))

lowest_strokes = get_lowest_strokes(distance, sorted(club_distances, reverse=True))
if lowest_strokes is None:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in {} strokes.".format(lowest_strokes))
