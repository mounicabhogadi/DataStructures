# def search(array, target):
#     # O(n)
#     for elem in array:
#         if target == elem:
#             return True
#
#     return False
#
#
# array = [23, 32, 45, 67, 98]
# target = 10
# retStatus = search(array, target)
# if retStatus == True:
#     print(f"target element {target} found ")
# elif retStatus == False:
#     print(f"target element {target} not found")
# else:
#     raise ValueError("Can be only true or false")
#



def classify_triangle(a, b, c):
    # Function to classify the type of triangle based on side lengths
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


test_cases = [(5, 5, 5), (3, 4, 3), (5, 5, 8), (7, 9, 10), (12, 15, 9), (2, 4, 6)]

for sides in test_cases:
    a, b, c = sides
    result = classify_triangle(a, b, c)
    print(f"Triangle with sides {a}, {b}, {c} is {result}.")

