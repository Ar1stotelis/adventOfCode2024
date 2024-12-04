

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

differences = [abs(l-r)for l,r in zip(left_column,right_column)]
difference = sum(differences)
print(f"Difference: {difference}")
