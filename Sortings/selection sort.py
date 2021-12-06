def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_ind = i

        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]

    return arr


val = [6, 72, 7, 3, 8, 78, 65, 1, 11]
print(selection_sort(val))