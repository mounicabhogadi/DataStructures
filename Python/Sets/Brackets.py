# Given a string of angle brackets, angles such as "><<><".
# Write a function that adds angle brackets to the beginning and
# end to make all angle brackets match and return it.
# The angle brackets "match" if for every < there is a corresponding > appearing after it in the string
# and for every > there is a corresponding < appearing before it in the string

def make_angle_brackets_match(angles):
    left_count = 0
    result = ""

    # Add leading angle brackets
    for char in angles:
        if char == '>':
            if left_count > 0:
                left_count -= 1
            else:
                result = '<' + result
        else:
            left_count += 1
        result += char

    # Add trailing angle brackets
    result += '>' * left_count

    return result


input_str = "><<><"
output_str = make_angle_brackets_match(input_str)
print(output_str)
