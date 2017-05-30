# Program to split a string by removing any subsequent occurrences non-distinct characters
# Hackerrank - merge_the_tools https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        chars = ""
        for j in range(i, i+k):
            if string[j] not in chars:
                chars += string[j]
                print(string[j], end='')
        print()  
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)