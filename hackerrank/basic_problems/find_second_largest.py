# You are given N numbers. Store them in a list and find the second largest number.
# 
# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.
# 
# Output Format 
# Output the value of the second largest number.
# 
# Sample Input
# 5
# 2 3 6 6 5
# 
# Sample Output
# 5


# First approach
def find_second_largest():
    # input() reads a line from input, converts it to a string (stripping a trailing newline).
    n = int(input())      
    # This below line reads a line, split it at whitespaces and applies int() to every element of the result.
    arr = list(map(int, input().split()))   
    arr.sort(reverse = True)
    i = 0
    while(arr[i] == arr[i+1]):
        i+=1
    print(arr[i+1])

if __name__ == '__main__':
    find_second_largest()


# Second Approach
if __name__ == '__main__':
    n = int(input())    
    arr = list(map(int, input().split()))
    M = max(arr)

    print(max(n for n in arr if n!=M))