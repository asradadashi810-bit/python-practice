# Count repeated items and find the common items of two lists

# How many times each number appears
numbers = [1, 2, 5, 2, 8, 5]
for i in range(len(numbers)):
    current = numbers[i]
    count = 0
    for j in range(len(numbers)):
        if numbers[j] == current:
            count += 1
    print(current, ":", count, "time")


# Common items of two lists
def common_in_both(numbers_1, numbers_2):
    result = []
    for i in range(len(numbers_1)):
        current = numbers_1[i]
        for j in range(len(numbers_2)):
            if numbers_2[j] == current and current not in result:
                result.append(current)
    return result


print(common_in_both([1, 8, 5, 10], [1, 10, 11, 21]))
