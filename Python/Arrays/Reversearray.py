class Reversearray:

    def reverseWithTemp(self, arr):
        #O(n) for time and space
        start_pos = 0
        end_pos = len(arr)-1
        while start_pos < end_pos:
            temp = arr[start_pos]
            arr[start_pos] = arr[end_pos]
            arr[end_pos] = temp
            start_pos += 1
            end_pos -= 1

    def reverse(self, arr):
        #O(n) for time and space
        start_pos = 0
        end_pos = len(arr)-1
        while start_pos < end_pos:
            arr[start_pos], arr[end_pos] = arr[end_pos], arr[start_pos]
            start_pos += 1
            end_pos -= 1



if __name__ == '__main__':
    ra = Reversearray()
    array = [1, 2, 3, 4, 5]
    print(f"Before Reverse {array}")
    ra.reverse(array)
    print(f"After reverse {array}")