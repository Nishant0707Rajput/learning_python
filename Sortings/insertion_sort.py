def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


print(insertion_sort([93, 67, 67, 4, 7, 23, 45, 27]))


