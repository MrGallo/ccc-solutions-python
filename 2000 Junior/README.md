# 2000 Junior Solutions

- [Junior 1 - Calendar](#junior-1---calendar)
- [Junior 2 - 9966](#junior-2---9966)
- [Junior 3/Senior 1- Slot Machines](#junior-3/senior-1---slot-machines)

## Junior 1 - Calendar
Simplified. See the `.py` file for more 'advanced' solve.
```python
inputs = input.split()
start = int(inputs[0])
days = int(inputs[1])

print("Sun Mon Tue Wed Thr Fri Sat")

# build list of calendar cells, padding the first ones as needed
calendar_spots = []
for _ in range(start-1):
    calendar_spots.append("")
for n in range(1, days+1):
    calendar_spots.append(n)

# Loop through calendar cells, printing 7 cells per row
for n in range(0, days+start-1, 7):
    week_str = ""
    for spot in calendar_spots[n:n+7]:
        week_str += "{:>3} ".format(spot)
    print(week_str[:-1])
```

**Topics**
- Datatypes
  - Convert from `str` to `int`
- Strings
  - `.split()`
  - `.format()`
    - Formatting specific padding and alignment
  - building new strings in a loop
  - slicing
- Lists
  - indicies
- Looping through a range
  - range(start, end, step)

## Junior 2 - 9966
```python
start = int(input())
end = int(input())

n = start
flippable = 0
while n <= end:
    split_n = list(str(n))
    replaced_n = []
    for char in split_n:
        if char == "0" or char == "1" or char == "8":
            replaced_n.append(char)
        elif char == "6":
            replaced_n.append("9")
        elif char == "9":
            replaced_n.append("6")
        else:
            replaced_n.append(None)

    if replaced_n[::-1] == split_n:
        flippable += 1

    n += 1

print(flippable)
```
**Topics**
- If statements
- Looping
  - from a number to another
  - through a list
  - Accumulator variable
- Lists
  - Splitting `str` into `List`
  - building lists in a loop
  - slicing

# Junior 3/Senior 1 - Slot Machines
```python
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
```

**Topics**
- Modulus
- If statements
- Loops
  - Counter variable
  - Accumulator variable
- Lists

