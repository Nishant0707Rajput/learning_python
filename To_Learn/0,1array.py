an_arr = [0, 1, 2, 1, 1, 2, 0, 0, 2, 0, 1, 1, 0, 2, 0]

def sort_01(arr):
    n = len(arr)
    x = 0
    y = 0
    for i in range(n):
        if arr[i] == 0:
            x += 1
        if arr[i] == 1:
            y += 1

    z = n - (x + y)

    for i in range(0, n):
        if i < x:
            arr[i] = 0
        elif i < x+y:
            arr[i] = 1
        else:
            arr[i] = 2
    # while i < j:
    #
    #     while i == 0 and i < j:
    #         i += 1
    #
    #     while j == 1 and i < j:
    #         j -= 1
    #
    #     if i < j:
    #         arr[i] = 0
    #         arr[j] = 1
    #         i += 1
    #         j -= 1


sort_01(an_arr)
print(an_arr)



