def merge(arr, lb, mid, ub):
    new_arr = [""]*(ub-lb+1)
    k = 0
    i = lb
    j = mid + 1

    while i <= mid and j <= ub:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        new_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= ub:
        new_arr[k] = arr[j]
        j += 1
        k += 1
    arr[lb:ub+1] = new_arr
    # print(new_arr)


def merge_sort(arr, lb, ub):
    # ub = r - 1
    if lb < ub:
        mid = lb + (ub-lb)//2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)
    return arr


val = [10, 72, 7, 3, 8, 1, 11, 9]
print(merge_sort(val, 0, len(val)-1))
print(val)




