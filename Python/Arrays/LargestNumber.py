# write a function that takes a list of numbers, numbers and
# then returns the largest number in the list. If no numbers in the list, return 0


def solution(numbers):
    if not numbers:
        return 0
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


numbers = [10, 5, 8, 15, 3]
largest_number = solution(numbers)
print(largest_number)
