
with open('day1input.txt', 'r') as file:
    lines = file.readlines()

left_column: list[int] = []
right_column: list[int] = []


for line in lines:

    numbers = line.split()
    if len(numbers) == 2:

        left, right = map(int,numbers)
        left_column.append(left)
        right_column.append(right)

left_column.sort()
right_column.sort()

sum = 0

for num in left_column:
    appearances = 0
    for n in right_column:
        if num == n:
            appearances += 1

    sum += (num * appearances)

print(sum)



