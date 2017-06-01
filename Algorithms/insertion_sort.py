# Program to implement insertion sort

# function for insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        # if elements of array[0..i-1] are greater than the key,
        # then move them to one position ahead of their current position
        j = i - 1
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


if __name__ == '__main__':
    arr = [2, 1, 0, 6, 5, 4, 8]
    result = insertion_sort(arr)
    print("Sorted array =", result) 