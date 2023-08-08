# Declare two variables `a` and `b`, assign integer values to them, and print their sum.
# - *Expected Output:* The sum of `a` and `b`.

a = 2
b = 13
print("The sum of 'a' and 'b' ", a + b)

# Create a variable `name` and assign your name to it. Print a greeting message using your name.
# - *Expected Output:* Greeting message with your name, e.g., "Hello, John!"

name = "Mounica"
print(f"Hello {name}!")

# Define a variable `pi` and assign the value of π (pi) to it. Print the value of `pi`.
# - *Expected Output:* The value of π (pi), e.g., 3.14159.

pi = 3.14159
print("The value of pi:", pi)

# Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string).
# Convert the input to a boolean and print its type.
# - *Expected Input:* "True" or "False"
# - *Expected Output:* The data type of the converted boolean.

is_raining_str = input("Please enter either 'True' or 'False': ")
is_raining = bool(is_raining_str)
print("The data type of the converted boolean is:", type(is_raining))

# Create a string variable `sentence` containing any sentence of your choice.
# Ask the user to input a number, convert it to an integer,
# and print the sentence repeated that number of times.
# - *Expected Input:* A number (e.g., "3")
# - *Expected Output:* The sentence repeated the specified number of times.

sentence = "It's a beautiful day"
num = input("Enter a number: ")
num_times = int(num)
print(sentence * num_times)


# Given two variables `x` and `y`, perform the following operations and print the results:
# - Addition of `x` and `y`.
# - Subtraction of `y` from `x`.
# - Multiplication of `x` and `y`.
# - Division of `x` by `y`.
# - `x` raised to the power of `y`.
# - The remainder when `x` is divided by `y`.
# - The floor division of `x` by `y`

x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** y)
print("Remainder:", x % y)
print("Floor Division:", x // y)


# Define a variable `value` and assign any numerical value to it.
# Ask the user to input a new value. Update the variable `value`
# with the new input and print the updated value.
# - *Expected Input:* A numerical value (e.g., "42")
# - *Expected Output:* The updated value of the variable.

value = 13
up_val = input("Enter a new value: ")
value = up_val
print("The updated value:", value)
