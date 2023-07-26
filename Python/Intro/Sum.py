# Program that takes positive numbers as input and calculate the sum of its digits
# 123: sum = 1+2+3 = 6
# 123 %10 = 3, 123/10 = 12
# 12 %10 = 2, 12/10 = 1
# 1 %10 = 1, 1/10 = 0

# x = int(input())
# sum_numbers = 0
# while x > 0:
#     sum_numbers += x % 10
#     x = x // 10
#
# print(sum_numbers)


# find the sum of 'n' natural numbers using for loop

n = int(input())
sum_numbers = 0
for num in range(n+1):
    sum_numbers += num
print(f"Sum of {n} natural numbers is: {sum_numbers}")

# 2

sum_formula = n*(n+1)//2
print(f"Sum of {n} natural numbers is: {sum_numbers}")



