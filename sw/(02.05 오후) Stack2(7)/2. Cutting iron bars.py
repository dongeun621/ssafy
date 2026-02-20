import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    cnt = 0
    result = 0
 
    for i, a in enumerate(arr):
        if a == '(':
            if arr[i+1] == '(':
                cnt += 1
                result += 1
            else:
                result += cnt
        else:
            if arr[i-1] == '(':
                continue
            else:
                cnt -= 1
 
 
    print(f'#{test_case} {result}')