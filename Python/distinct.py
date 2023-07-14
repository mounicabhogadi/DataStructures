#Have the function DistinctList(arr) take the array of numbers stored in arr and
# determine the total number of duplicate entries.
# For example if the input is [1, 2, 2, 2, 3] then
# your program should output 2 because there are two duplicates of one of the elements.

def DistinctList(arr):

    duplicate = 0;
    seen = set()

    for num in arr:
        if num in seen:
            duplicate += 1
        else:
            seen.add(num)
    return duplicate


# keep this function call here
arr = [1, 2, 2, 2, 3]
print(DistinctList(arr))