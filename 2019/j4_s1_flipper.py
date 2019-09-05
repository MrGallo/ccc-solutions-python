from collections import Counter

def vertical_flip(index: int):
    if index % 2 == 0:
        return index+1
    return index - 1


def horizontal_flip(index: int):
    return (index + 2) % 4


FUNC_MAP = {
    "H": horizontal_flip,
    "V": vertical_flip
}

flip_counts = Counter(input())
indexes = range(4)

for flip_type in FUNC_MAP.keys():
    if flip_counts[flip_type] % 2 == 1:
        indexes = map(FUNC_MAP[flip_type], indexes)

result_list = list(map(lambda x: x+1, indexes))

print(*result_list[:2])
print(*result_list[2:])
