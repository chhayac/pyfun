# Program to find a peak element in an array using divide and conquer approach.
# Complexity is O(log n)
# Example:
# Input: 
# [10,30,50,90,20]
# 
# Output:
# Peak element is 90

def peak_find(arr, low, high, n):
    if high >= low:
        # find index of middle element
        mid = low + (high - low)//2

        # compare middle element with its neightbours (if neighbours exist)
        if ((mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid])):
            return mid

        # If middle element is not a peak element and its left neighbour is greater than it, then left half must 
        # have a peak element  
        elif (mid > 0 and arr[mid -1] > arr[mid]):
            return peak_find(arr, low ,mid - 1, n)
        
        # If middle element is not a peak element and its right neighbour is greater than it, then right half
        # must have a peak element
        else:
            return peak_find(arr, mid + 1, high, n)


if __name__ == '__main__':
    arr = [10,30,50,90,20]
    n = len(arr)
    low, high = (0, n-1)
    peak = peak_find(arr, low, high, n)
    print("Peak element is", arr[peak])