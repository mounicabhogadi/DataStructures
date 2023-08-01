arr = [2, 3, 4, 5, 6, 7, 8]
print(arr)

arr_range = list(range(2, 9))
print(arr_range)

arr_nul = [-1] * 8
print(arr_nul)

# new_list = [expression for item in iterable if condition]
arr_listcomp = [x for x in arr if x % 2 == 0]
print(arr_listcomp)


# create a list of numbers with squares of the following numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [x*x for x in numbers]
print(squared_numbers)

# print odd numbers from the given numbers list
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)