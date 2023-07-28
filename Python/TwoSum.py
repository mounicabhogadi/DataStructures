# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# 1
from typing import List

list_numbers = [3, 2, 4]
target = 6
found = False
for i in range(len(list_numbers)):
    for j in range(len(list_numbers)):
        if i != j and list_numbers[i] + list_numbers[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break

# 2
# list_numbers[i] + list_numbers[j] == target
# a + b = t
# b = t - a
# list_numbers = [3, 2, 4]
# target = 6
# b = 6 - 3 = 3
# b = 6 - 2 = 4

# if elements in the array doesn't repeat
dict_of_number = {}
for index in range(len(list_numbers)):
    dict_of_number[list_numbers[index]] = index
print(dict_of_number)

for key in dict_of_number:
    if key != target - key and target - key in dict_of_number:
        print(dict_of_number[key], dict_of_number[target - key])
        break

# 3 using function and return statement (leetcode submission)

def twoSum(self, nums: List[int], target: int) -> List[int]:
    found = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] + nums[j] == target:
                return(i,j)
                found = True
                break
        if found:
            break
