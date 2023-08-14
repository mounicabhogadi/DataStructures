
def bsearch(array, target, left, right):
    """
    :param array: List of elements
    :param target:integer element
    :param left:array[index]
    :param right:array[index]
    :return:boolean
    """
    if left > right:
        return False
    mid = (left + right) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return bsearch(array, target, mid + 1, right)
    else:
        return bsearch(array, target, left, mid-1)



array = [12, 13, 34, 56, 87]
target = 12
retStatus = bsearch(array, target, 0, len(array)-1)

if retStatus:
    print(f"Target element {target} found")
else:
    print(f"Target element {target} not found")
