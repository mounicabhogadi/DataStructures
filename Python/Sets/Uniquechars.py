str_a = "ababa"
set_string = set(str_a)
print(set_string)

# not using set()
# search O(1)
# add O(1)
# delete O(1)
a_dict = {}
for c1 in str_a:
    if c1 not in a_dict:
        a_dict[c1] = True
print(list(a_dict.keys()))

# do not use sets and dicts
# search O(n) if not sorted, O(n+nlogn) if sorted
# add O(1)
# delete O(logn) +O(1) = O(logn)

a_arr = []
for c1 in str_a:
    if c1 not in a_arr:
        a_arr.append(c1)
print(a_arr)