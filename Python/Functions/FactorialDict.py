fact_dict = {0: 1}


def better_fact(n):
    if n in fact_dict:
        return fact_dict[n]
    fact_dict[n] = n * better_fact(n - 1)
    return fact_dict[n]


num = 5
fact_array = []
# Time complexity O(n)
for n in range(num + 1, -1, -1):
    fact_array.append(better_fact(n))

print(fact_array)
