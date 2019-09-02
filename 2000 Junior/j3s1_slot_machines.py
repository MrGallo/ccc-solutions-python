quarters = int(input())
first_state = int(input())
second_state = int(input())
third_state = int(input())

machines_state = [first_state, second_state, third_state]

plays = 0
while quarters > 0:
    current_machine_index = plays % 3
    quarters -= 1
    machines_state[current_machine_index] += 1
    if current_machine_index == 0 and machines_state[current_machine_index] == 35:
        machines_state[current_machine_index] = 0
        quarters += 30
    elif current_machine_index == 1 and machines_state[current_machine_index] == 100:
        machines_state[current_machine_index] = 0
        quarters += 60
    elif current_machine_index == 2 and machines_state[current_machine_index] == 10:
        machines_state[current_machine_index] = 0
        quarters += 9
    plays += 1

print("Martha plays {} times before going broke.".format(plays))
