# create an array to store the expenses for each day of the week and
# add basic operations to add expense and retrieve useful information. Do the following :
# Highest and lowest expense
# Average weekly expense
# Total weekly expense

weekly_expenses = [230, 127, 346, 476, 100, 700]
weekly_expenses.append(200)
print(weekly_expenses)
highest_expense = max(weekly_expenses)
lowest_expense = min(weekly_expenses)
print(f"Highest and Lowest expenses are: {highest_expense}, {lowest_expense}")
average_expense = sum(weekly_expenses) / len(weekly_expenses)
total_expense = sum(weekly_expenses)
print(f"Average weekly expense: {average_expense}")
print(f"Total weekly expense: {total_expense}")
print("\n")


# 2

print("#Second solution#")

highest = weekly_expenses[0]
lowest = weekly_expenses[0]
total = 0
for i in weekly_expenses:
    if i > highest:
        highest = i
    elif i < lowest:
        lowest = i
    total += i

average = total / len(weekly_expenses)

print("Highest and Lowest expenses are:", highest, ",", lowest)
print(f"Average weekly expense:", average)
print(f"Total weekly expense:", total)
