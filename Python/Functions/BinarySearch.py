
def bsearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


array = [12, 13, 34, 56, 87]
target = 87
retStatus = bsearch(array, target)

if retStatus:
    print(f"Target element {target} found")
else:
    print(f"Target element {target} not found")
