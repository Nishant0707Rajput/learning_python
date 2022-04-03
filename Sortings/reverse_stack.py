def ins(arr, val):
    if len(arr) == 0:
        arr.append(val)
        return arr
    var = arr.pop()
    arr = ins(arr, val)
    arr.append(var)
    return arr


def rever_stack(arr):
    if len(arr) == 1:
        return arr
    val = arr.pop()
    arr = rever_stack(arr)
    arr = ins(arr, val)
    return arr


print(rever_stack([4,3,1,12,7,42]))