def ins(arr, ele):
    if len(arr) < 1 or arr[-1] < ele:
        return arr + [ele]
    v = arr.pop()
    arr = ins(arr, ele)
    arr = arr + [v]
    return arr


def recur_sort(arr):
    if len(arr) == 1:
        return arr
    val = arr.pop()
    arr = recur_sort(arr)
    arr = ins(arr, val)
    return arr


var = [2, 7, 4, 9, 0, 5]
print(recur_sort(var))


