def main():
    num_lines = int(input())
    lines = [input() for _ in range(num_lines)]
    for line in lines:
        print(encode(line))


def encode(line: str):
    encoded_string = ""
    current_char = None
    current_char_count = 0
    for char in line:
        if not current_char:
            current_char = char
            current_char_count += 1
        elif current_char == char:
            current_char_count += 1
        else:
            encoded_string += f"{current_char_count} {current_char} "
            current_char = char
            current_char_count = 1
    encoded_string += f"{current_char_count} {current_char}"
    return encoded_string


def tests():
    assert encode("hhh") == "3 h"
    assert encode("hhhh") == "4 h"
    assert encode("hhhhrrr") == "4 h 3 r"
    assert encode("hhhhrrr6666") == "4 h 3 r 4 6"


if __name__ == '__main__':
    main()




