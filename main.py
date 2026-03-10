def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        midpoint = (left + right) // 2
        midpoint_value = values[midpoint]

        if midpoint_value == target:
            return midpoint
        if midpoint_value < target:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return -1


if __name__ == "__main__":
    sample = [2, 4, 6, 8, 10, 12, 14]
    target = 10
    print("Values:", sample)
    print("Target:", target)
    print("Index:", binary_search(sample, target))
