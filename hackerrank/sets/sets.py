# Program to compute average height of the plants.

# Input Format
# The first line contains the integer, N , the total number of plants.
# The second line contains the N space separated heights of the plants.

# Output Format
# Output the average height value on a single line.

# Sample Input
# 10
# 161 182 161 154 176 170 167 171 170 174

# Sample Output
# 169.375

def average(array):
    average = sum(array) / len(array)
    return average  
    
if __name__ == "__main__":
    N = int(input())
    arr = set(map(int, input().split()))
    result = average(arr)
    print(result)