# print  first 10 natural numbers except 5

target_number = 5

for i in range(1, 11):
    if target_number == i:
        continue
    print(i)
