def bubble_Sort(data: list) -> None:
    """SORTS the data at it's place"""

    n = len(data)
    count = 0

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            count += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        print(data)
        if not swapped:
            break

    print("Comparison_Count--",count)


bubble_Sort([1, 2, 3, 4, 6, 5, 7 ])
