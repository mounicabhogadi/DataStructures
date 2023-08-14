# Write a Python program that calculates the area of various geometric shapes
# using functions. The program should provide a menu to the user to choose a shape,
# input the necessary parameters, and then display the calculated area.


import math


# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2


# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width


# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height


# Function to calculate the area of a square
def square_area(side):
    return side ** 2


# Main function
def main():
    print("Select a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
    elif choice == 4:
        side = float(input("Enter the side length of the square: "))
        area = square_area(side)
    else:
        print("Invalid choice")
        return

    print(f"The area of the selected shape is: {area}")


if __name__ == "__main__":
    main()
