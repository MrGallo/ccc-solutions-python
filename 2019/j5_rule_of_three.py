# 14/15 Solution.
# TLE On the last point :(
# Perhaps memoize step lists for particular strings?

rule_pairs = {number: input().split() for number in range(1, 4)}


def do_substitution(steps_remaining, current_string, final_string):
    step_list = []

    if steps_remaining == 0 and current_string == final_string:
        return step_list
    elif steps_remaining == 0:
        return []

    for i, char in enumerate(current_string):
        for rule_num, (frm, to) in rule_pairs.items():
            substr = current_string[i:i + len(frm)]
            if substr == frm:
                new_string = current_string[:i] + to + current_string[i+len(frm):]
                step_list.append([rule_num, i+1, new_string])
                result_step_list = do_substitution(steps_remaining-1, new_string, final_string)
                if result_step_list:
                    return step_list + result_step_list
                else:
                    step_list = []


steps, initial, final = input().split()
step_list = do_substitution(int(steps), initial, final)
for step in step_list:
    print(*step)


"""AA AB
AB BB
B AA
4 AB AAAB"""