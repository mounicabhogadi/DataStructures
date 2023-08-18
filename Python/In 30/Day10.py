
def positiveornegative(num):
    if num >= 1:
        print("Positive")
    elif num <= -1:
        print("Negative")
    elif num == 0:
        print("Zero")


# even or odd | and | positive or negative

num = int(input("Enter a number: "))
positiveornegative(num)
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# find leap year or not and also print number of days in february for that year


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days_in_february(year):
    if is_leap_year(year):
        return 29
    return 28


# Replace the_year with the year you want to check
the_year = int(input("Enter year: "))

if is_leap_year(the_year):
    print(f"{the_year} is a leap year.")
    print(f"February has {days_in_february(the_year)} days.")
else:
    print(f"{the_year} is not a leap year.")
    print(f"February has {days_in_february(the_year)} days.")