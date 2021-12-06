def bubble_sort(arr: list) ->list:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


val = [6, 72, 7, 3, 8, 1, 11]
print(bubble_sort(val))