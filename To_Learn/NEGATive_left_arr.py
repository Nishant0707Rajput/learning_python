def move_to_left(arr):
    # j = 0
    n = len(arr)
    # for i in range(n):
    #     if arr[i] < 0:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         j += 1
#     Using two pointer now
    left = 0
    right = n - 1
    while left < n and right > 0:


array = [0, 8, 3, 4, -1, -3, -8, -7]
move_to_left(array)
print(array)

