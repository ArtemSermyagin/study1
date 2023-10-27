import statistics


def nums(numbers):
    average = statistics.mean(numbers)
    print(average)
    list_1 = []
    for number in numbers:
        if number < average:
            list_1.append(number)
        else:
            break
    return list_1


numbers = [1, 2, 3, 4, 5]
print(nums(numbers))
