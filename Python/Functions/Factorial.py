# num
# 0.....num factorials
# if num = 5
# output should be 1!, 2!, 3!, 4!, 5!

def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    return fact


num = 5
fact_array = []
# Time complexity O(n2)
for n in range(0, num + 1):
    fact_array.append(factorial(n))

print(fact_array)


# Time complexity O(n)

def factorial_best(num):
    fact = {0: 1, 1: 1}
    result = []

    for i in range(2, num + 1):
        fact[i] = fact[i - 1] * i

    for i in range(num, 0, -1):
        result.append(f"{i}! = {fact[i]}")

    return result

num = 5
output = factorial_best(num)
print(', '.join(output))




# O(n)
def facthw(n):
    num_array = []
    for i in range(0, n + 1):
        num_array.append(i)

    fact = 1
    fact_result_array = []
    for j in num_array:
        if j == 0:
            fact_result_array.append(1)
        else:
            fact = fact * j
            fact_result_array.append(fact)
    return fact_result_array


print(facthw(6))
