def binary_search(arr: list, element: int):
    low = 0
    high = len(arr)-1

    while low != high:
        bin_form = low + (high - low) // 2
        if element == arr[bin_form]:
            print(f"Element found at {bin_form} index in the array")
            break
        elif element > arr[bin_form]:
            low += 1
        else:
            high -= 1
    else:
        print(f"{element} not found in the array.")


new_arr = [2, 3, 4, 10, 40, 89]
to_be_searched = None
while to_be_searched != -1:
    to_be_searched = int(input("Enter the number to be searched > "))
    if to_be_searched == -1:
        continue
    binary_search(new_arr, to_be_searched)