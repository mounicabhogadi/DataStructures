# linear search to find a target number from the input list.
# If the target number is present, print index

list_numbers = [12, 13, 3, 45, 30, 98, 96]
target_number = 3
found_target = False
for index in range(len(list_numbers)):
    if list_numbers[index] == target_number:
        print(f"{target_number} found at index {index}")
        found_target = True
        break

if not found_target:
 print(f"{target_number} not found")

