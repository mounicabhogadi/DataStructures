# even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# largest number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 >= num2:
    print(num1)
else:
    print(num2)


# vowels or consonants

character = input("Enter a character: ")
# Convert the character to lowercase to handle both cases
character = character.lower()

if character in ['a', 'e', 'i', 'o', 'u']:
    print("vowel")
else:
    print("consonant")

# Leap year or not

year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a Leap year")


# Pass or Fail

grade = input("Enter a grade: ")
grade = grade.upper()
if grade in ['A', 'B', 'C', 'D']:
    print("Pass")
elif grade in ['F']:
    print("Fail")
else:
    print("Invalid Grade")





