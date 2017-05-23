# In this problem, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)]) == sub_string:
            count+=1
    return print(count)

if __name__ == '__main__':
    string = input()
    sub_string = input()
    count = count_substring(string, sub_string)
