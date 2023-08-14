def search(array, target):
    # O(n)
    for elem in array:
        if target == elem:
            return True

    return False


array = [23, 32, 45, 67, 98]
target = 10
retStatus = search(array, target)
if retStatus == True:
    print(f"target element {target} found ")
elif retStatus == False:
    print(f"target element {target} not found")
else:
    raise ValueError("Can be only true or false")
