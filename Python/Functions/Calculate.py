# Write a method Calculate Statistics that calculates total and average of an array of integers
from numpy import mean

integers = []


def calculate_statistics(integers):
    total = 0
    for i in range(len(integers)):
        # print(i)
        total += integers[i]

    # 2
    # for i in integers:
    #     total += i
    average = total / len(integers)
    return total, average

def calculate_statistics_predefined(integers):
    return sum(integers), mean(integers)


integers = [2, 3, 4, 5, 6, 7]
total, average = calculate_statistics_predefined(integers)
print(f"Total: {total}, Average: {average}")