# 1. print numbers from 1 to 5

for num in range(1, 6):
    print(num)

# 2. calculate sum of numbers from 1 to 10

sum = 0
for num in range(1, 11):
    sum += num
    num += 1
print(f"Sum of numbers from 1 to 10 is: {sum}")


# 3. print each character in a given string

input_string = input("Enter a string: ")
for char in input_string:
    print(char)

# 4. print first 10 even numbers

for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# 5. double each number in the sequence

numbers = [1, 3, 4, 5, 6]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(f"Double of {numbers} is: {doubled_numbers}")