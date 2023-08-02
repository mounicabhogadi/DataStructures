grades = [32, 45, 65, 87, 98]

# print last elements
print(grades[-1])

# You are given an array of integers.
# Implement a function to reverse the elements of the array using negative indexing.

reverse_grades = []
for index in range(len(grades)-1, -1, -1):
    reverse_grades.append(grades[index])
print(f"Reverse grades: {reverse_grades}")

reverse_grades = [grades[x] for x in range(len(grades)-1, -1, -1)]
print(f"List comprehension Reverse: {reverse_grades}")

# Reverse an array in place
reverse_index = -1
for index in range(0, len(grades)//2):
    reverse_index -= index
    grades[index], grades[reverse_index] = grades[reverse_index], grades[index]

print(f"Reverse array in place: {grades}")

