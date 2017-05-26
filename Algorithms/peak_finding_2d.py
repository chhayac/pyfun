# Program to find peak element in 2-D array using divide and conquer approach
# Complexity is O(nlog(m)) where n is the number of rows and m is the number of columns
# Example: 
# Input: 
# 43      90      24      76      34
# 32      8       70      36      24
# 92      6       12      34      20
# 18      39      37      43      63
# 
# Output:
# Peak element in 2-D array is 70

# Note: The algorithm finds any of the peak elements if multiple peak elements are present.

import random

def peakFind2D(arr, low, high):

    # find the index of middle column 
    j = (low + high) //2

    # find the index of maximum value present in the middle column
    middle_column = [i[j] for i in arr]
    i = middle_column.index(max(middle_column))

    # check if maximum value of the column is a peak element
    if ((j-1 >= 0 and arr[i][j] >= arr[i][j-1]) and \
        (j+1 < len(arr[i]) and arr[i][j] >= arr[i][j+1])):
        return arr[i][j]
    
    # else pick left columns if the greater value is present on the left side
    elif (j > 0 and arr[i][j-1] > arr[i][j]):
        high = j-1
        return peakFind2D(arr, low, high)

    # else pick right columns if the greater value is present on the right side
    elif (j+1  < len(arr[i]) and arr[i][j+1] > arr[i][j]):
        low = j+1
        return peakFind2D(arr, low, high)
    return arr[i][j]

# generate a random 2-D matrix
def randomMatrix():
    i = random.randrange(1, 11)
    j = random.randrange(1, 11)
    mat = [[random.randrange(0, 101) for y in range(j)] for x in range(i)]
    return mat

def printMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end='\t')
        print()

if __name__ == '__main__':
    arr = randomMatrix()
    printMatrix(arr)
    low = 0
    high = len(arr[0]) - 1 
    result = peakFind2D(arr, low, high)
    print("Peak element in 2-D array is",result)
 
   