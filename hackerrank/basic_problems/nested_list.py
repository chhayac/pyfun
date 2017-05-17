# Given the names and grades for each student in a Physics class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N , the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, 
# and the second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; 
# if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output
# Berry
# Harry

if __name__ == '__main__':
    n = int(input())
    marksheet = [[input(),float(input())] for _ in range(n)]
    
    if n>=2 and n<=5:
        second_largest = sorted(set([marks for name, marks in marksheet]))[1]
        print('\n'.join([a for a,b in sorted(marksheet) if b == second_largest]))