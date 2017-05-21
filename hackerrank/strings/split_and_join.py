# In Python, a string can be split on a delimiter.

# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']

# Joining a string is simple:
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 

# Task 
# You are given a string. Split the string on a " " (space) delimiter 
# and join using a - hyphen.

# Sample Input
# this is a string   

# Sample Output
# this-is-a-string

def split_and_join(string):
    print("-".join(string))

if __name__ == '__main__':
    line = input().split()
    split_and_join(line)

# one line to print the output without using function
# print("-".join(input().split()))