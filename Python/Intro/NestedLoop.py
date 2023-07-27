# print combinations and iteration count

# sum = 0
# for i in range(1, 6):
#     for j in range(1, 3):
#         sum += 1
#         print(i, j)
#
# print(sum)


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")


# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")

