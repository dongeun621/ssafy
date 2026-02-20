import sys

sys.stdin = open('sample_input6.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    t, n = input().split()
    t = int(t[1:])
    n = int(n)
 
    arr = input().split()
    text_arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_arr = []
 
    for i in range(n):
        for j in range(10):
            if arr[i] == text_arr[j]:
                arr[i] = j
    arr.sort()
 
    for i in range(n):
        for j in range(10):
            if arr[i] == j:
                arr[i] = text_arr[j]
 
    print(f'#{test_case}')
    print(*arr)