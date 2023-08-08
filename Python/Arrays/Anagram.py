word1 = "cat"
word2 = "tac"

result_arr1 = [0]*26
result_arr2 = [0]*26

# print(ord('a'))

for c1 in word1:
    index1 = ord(c1) - ord('a')
    # print(index)
    result_arr1[index1] += 1
# print(result_arr1)

for c2 in word2:
    index2 = ord(c2) - ord('a')
    # print(index)
    result_arr2[index2] += 1
# print(result_arr2)


if result_arr1 == result_arr2:
    print("Anagram")
else:
    print("Not Anagram")
