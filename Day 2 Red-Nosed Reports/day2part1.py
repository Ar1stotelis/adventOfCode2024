
def is_safe(nums):

    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i -1])
        if diff < 1 or diff > 3:
            return False

    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        return True
    else:
        return False


def main ():
    counter = 0

    with open('day2input.txt' , 'r') as file:

        reports = [list(map(int, line.split())) for line in file]



        for report in reports:
            if is_safe(report):
                counter += 1


    print(counter)


if __name__ == "__main__":

    main()