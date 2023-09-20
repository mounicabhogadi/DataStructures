# strings are not empty or None.
class Solution:
    def check_for_rotation(self, str1, str2):
        if len(str1) != len(str2):
            return False

        for r1 in range(len(str2)):
            if str1 == self.rotation(str2, r1):
                return True
        return False

    def rotation(self, str, rnumber):
        # rotation logic
        rotated_str = str[(len(str) - rnumber):] + str[:len(str) - rnumber]
        return rotated_str

    def new_check(self, str1, str2):
        if len(str1) != len(str2):
            return False
        temp_str = str1 + str1
        if str2 in temp_str:
            return True
        else:
            return False

    def isSubstring(self, str1, str2):
        str1_start_pos = 0
        str2_start_pos = 0
        while str1[str1_start_pos] != str2[str2_start_pos]:
            str2_start_pos += 1
        while str1_start_pos < len(str1):
            if str1[str1_start_pos] != str2[str2_start_pos]:
                return False
            str1_start_pos += 1
            str2_start_pos += 1
        return False



if __name__ == '__main__':
    sol = Solution()
    if sol.new_check("waterbottle", "erbottlewat"):
        print("Rotations")
    else:
        print("Not Rotations")