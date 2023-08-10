# Given a string s, find the length of the longest
# substring that contains no repeated characters

def longest_substring_length(s):
    if not s:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}  # To track the index of each character

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        max_length = max(max_length, end - start + 1)
        char_index_map[s[end]] = end

    return max_length


s = "abcabcbb"
length = longest_substring_length(s)
print(length)
