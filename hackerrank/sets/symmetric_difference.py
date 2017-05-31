# Task 
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
#
# Input Format
# The first line of input contains an integer, M. 
# The second line contains M space-separated integers. 
# The third line contains an integer, N. 
# The fourth line contains N space-separated integers.
#
# Output Format
# Output the symmetric difference integers in ascending order, one per line.

# Sample Input
# 4
# 2 4 5 9
# 4
# 2 4 11 12

# Sample Output
# 5
# 9
# 11
# 12

# ^ symbol can also be used to compute the symmetric difference of two sets.


if __name__ == '__main__':
    # take input from stdin 
    M = input();m = input().split()    
    N = input();n = input().split()

    # compute the symmetric difference of 2 sets & create a list, then sort the list converting 
    # each element of list to integer & joining with newline 
    print("\n".join(sorted(list(set(m) ^ set(n)), key = int)))