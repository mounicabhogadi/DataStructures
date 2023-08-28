# 1. print numbers from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1


# 2. print sum input 4, [4+3+2+1]
# output 10

num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print(sum)


# 3. print even numbers from 2 to 10

num = 2

while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# 4. Enter a number until user gives a negative number

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break

# 5. print numbers from 10 to 1

num = 10
while num >= 1:
    print(num)
    num -= 1


# 6. Create a while loop that asks user to guess a secret number and
# continues until the correct number is guessed


target = int(input("Enter a secret number: "))
while True:
    num = int(input("Guess the secret number: "))
    if num == target:
        print("You guessed right!!")
        break

# 7. Factorial

num = int(input("Enter a number: "))
i = 1
mul = 1
while i <= num:
    mul *= i
    i += 1
print(f"Factorial of {num} is: {mul}")


# 8. Fibonacci series

n = int(input("Enter the value of n: "))

fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= n:
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)

print("Fibonacci series up to", n, ":", fibonacci)


# 9. Write a while loop that reads numbers from the user until they enter 0.
# Then it prints the sum of all the entered numbers

sum = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    sum += num

print(f"Sum of entered numbers: {sum}")

# 10. print squares of numbers from 1 to 5

num = 1
while num <= 5:
    square = num * num
    print(f"Square of {num} is: {square}")
    num += 1


