def move_neg(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        while arr[left] < 0:
            left += 1
        while arr[right] > 0:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[right] = arr[right], arr[left]


array = [-1,20, -7,4,9, -4, 8, 6,-9, 2, 4]
move_neg(array)
print(array)