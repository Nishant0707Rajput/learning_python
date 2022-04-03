def delk(arr, k):
    if len(arr) == k:
        arr.pop()
        return arr
    var = arr.pop()
    arr = delk(arr, k)
    arr += [var]
    return arr


print(delk([2,3,5,6,7,9],4))