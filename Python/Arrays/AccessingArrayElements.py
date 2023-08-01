# print numbers and corresponding indices
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in range(0, len(numbers)):
    print(index, numbers[index])


# using enumerate function
for index, value in enumerate(numbers):
    print(index, value)


