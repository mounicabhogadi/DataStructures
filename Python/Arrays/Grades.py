# You are tasked with building a student grades tracker. Create an array to store
# the grades of a class for a particular subject and implement functions to perform basic operations.
# Create an array to store the grades of five students in a subject.
# Calculate the average marks of the class
# find and return the highest grade obtained in the class.
# find and return the lowest grade obtained in the class.
# count and return the number of passing grades
# count and return the number of failing

grades = [32, 45, 65, 87, 98]
total = 0
for grade in grades:
    total += grade
print(f"Total: {total}")

# Calculate the average marks of the class
average = int(total / len(grades))
print(f"Average: {average}")

# find and return the highest grade obtained in the class.
highest = grades[0]
for grade in grades:
    if highest > grade:
        highest = grade
print(f"Highest grade in the class: {highest}")

# find and return the lowest grade obtained in the class.
lowest = grades[0]
for grade in grades:
    if lowest < grade:
        lowest = grade
print(f"Lowest grade in the class: {lowest}")


# count and return the number of passing grades
# pass_count = 0
# fail_count = 0
# for grade in grades:
#     if grade < 35:
#         fail_count += 1;
#     else:
#         pass_count += 1;
#
# print(f"Pass count: {pass_count}")
# print(f"Fail count: {fail_count}")



fail_count = 0
for grade in grades:
    if grade < 35:
        fail_count += 1;

print(f"Pass count: {len(grades) - fail_count}")
print(f"Fail count: {fail_count}")


# subgrades

sub_array = grades[2:5]
print(sub_array)

# deleting a sub array
del grades[2:3]
print(grades)
