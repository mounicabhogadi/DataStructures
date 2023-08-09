def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b

# Time complexity O(n)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
print(f"Factorial of {n}:", factorial(n))


print(sum(1, 2))
print(multiply(3, 2))
print(sum(1, 8))
