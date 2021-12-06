def sort_012(arr):
    left = 0
    n = len(arr)
    right = len(arr) - 1
    mid = 0
    while mid < right:
        if arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            left += 1
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
            # mid += 1
        else:
            mid += 1


array = [0, 2, 1, 2, 0]
sort_012(array)
print(array)