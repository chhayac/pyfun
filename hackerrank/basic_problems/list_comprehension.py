# list comprehensions! 
# You are given three integers X,Y,Z and  representing 
# the dimensions of a cuboid along with an integer N. You have to print a list of all 
# possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k is not equal to n . Here, 
# 0<=i<=X, 0<=j<=Y, 0<=k<=Z

# Input Format
# Four integers  and  each on four separate lines, respectively.

# Constraints
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2

#Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 

if __name__ == '__main__':

    x,y,z,n = (int(input()) for _ in range(4))
    listofNumbers = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
    print(listofNumbers)