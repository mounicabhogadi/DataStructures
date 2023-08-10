# Suppose, you are given binary tree represented as an array [3, 6, 2, 9, -1, 10].
# write a function that determines if left or right of the tree is the largest.
# The size of each branch is the sum of node values.
# The function should return the string "Right" if the right side is larger and
# "left" if the left side is larger

def find_larger_side(tree):
    if not tree:
        return "Neither"  # Empty tree

    def calculate_sum(index):
        if index >= len(tree) or tree[index] == -1:
            return 0
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        return tree[index] + calculate_sum(left_child_index) + calculate_sum(right_child_index)

    root_index = 0
    left_sum = calculate_sum(2 * root_index + 1)
    right_sum = calculate_sum(2 * root_index + 2)

    if left_sum > right_sum:
        return "Left"
    elif right_sum > left_sum:
        return "Right"
    else:
        return "Neither"  # Both sides have equal sum


# Test the function
binary_tree = [3, 6, 2, 9, -1, 10]
result = find_larger_side(binary_tree)
print("The larger side is:", result)
