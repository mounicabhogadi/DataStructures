# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1_dict = {}
        word2_dict = {}
        # O(n) + O(n) + O(n) + O(1) = O(3n+1) = O(n)
        if len(s) != len(t):
            return False

        for c1 in s:
            if c1 not in word1_dict:
                word1_dict[c1] = 1
            else:
                word1_dict[c1] += 1
        print(word1_dict)

        for c2 in t:
            if c2 not in word2_dict:
                word2_dict[c2] = 1
            else:
                word2_dict[c2] += 1
        print(word2_dict)

        anagram_found = True
        for key1 in word1_dict:
            if key1 not in word2_dict:
                anagram_found = False
                break
            else:
                if word1_dict[key1] != word2_dict[key1]:
                    anagram_found = False
                    break

        return anagram_found