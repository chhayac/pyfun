def find_second_largest():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    i = 0
    while(arr[i] == arr[i+1]):
        i+=1
    print(arr[i+1])

if __name__ == '__main__':
    find_second_largest()