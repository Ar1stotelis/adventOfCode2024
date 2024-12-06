def is_safe(nums):

    def is_valid_diff(nums):
        # Check if all adjacent differences are between 1 and 3.
        return all(1 <= abs(nums[i] - nums[i - 1]) <= 3 for i in range(1, len(nums)))

    def is_sorted_and_valid(nums):
        # Check if a list is sorted (ascending or descending) and valid.
        return (nums == sorted(nums) or nums == sorted(nums, reverse=True)) and is_valid_diff(nums)


    # Check if removing one level makes the list safe
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i + 1:]  # Remove the i-th element
        if is_sorted_and_valid(new_nums):
            return True

    return False  # Not safe if none of the above conditions are satisfied


def main():
    safe_count = 0

    with open('day2input.txt', 'r') as file:
        # Parse the input into a list of lists of integers
        reports = [list(map(int, line.split())) for line in file]

        # Check each report
        for report in reports:
            if is_safe(report):
                safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()
