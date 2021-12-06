def partition(arr: list, lb: int, ub: int) -> int:
    start = lb
    end = ub-1
    pivot = arr[lb]
    while start < end:
        while arr[start] <= pivot and start < ub-1:
            start += 1
        while arr[end] > pivot and end >= lb:
            end -= 1
        if start > end:
            break
        arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[lb] = arr[lb], arr[end]
    return end


def quick_sort(arr: list, lb: int, ub: int) -> list:
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc-1)
        quick_sort(arr, loc+1, ub)
    return arr


val = [2, 1, 6, 10, 4, 1, 3, 9, 7]
quick_sort(val, 0, len(val))
print(val)
#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self, arr,low,high):
        # code here
        if low < high:
            loc = self.partition(arr, low, high)
            self.quickSort(arr, low, loc-1)
            self.quickSort(arr, loc+1, high)
        # return arr

    def partition(self, arr, low, high):
        # code here
        start = low
        end = high
        pivot = arr[low]
        while start < end:
            while arr[start] <= pivot and start < high:
                start += 1
            while arr[end] > pivot:
                end -= 1
            if start > end:
                break
            arr[start], arr[end] = arr[end], arr[start]

        arr[low],arr[end] = arr[end], arr[low]
        return end



#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":

    n = 10
    arr = [2, 1, 6, 10, 4, 1, 3, 9, 7,1]
    Solution().quickSort(arr, 0, n-1)
    for i in range(n):
        print(arr[i], end=" ")
    # print()

# } Driver Code Ends