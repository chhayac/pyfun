# Task 
# Read a given string, change the character at a given index and then print the modified string.

# Input Format 
# The first line contains a string, S. 
# The next line contains an integer i, denoting the index location and a character separated by a space.

# Output Format 
# Replace the character at index i with character c.

# Sample Input
# abracadabra
# 5 k

# Sample Output
# abrackdabra

# Approach I : Convert the string to a list and then change the value.
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return (print("".join(l)))

if __name__ == '__main__':
    string = input()
    i, c = input().split()
    result = mutate_string(string,int(i),c)


# Approach II : Slice the string and join it back.
def mutate_string(string, position, character):
    return s[:int(i)]+c+s[int(i)+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


