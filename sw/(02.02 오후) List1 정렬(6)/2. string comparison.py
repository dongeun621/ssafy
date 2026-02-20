import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a = input()
    b = input()
    n = len(a)
    result = 0
    for idx, val in enumerate(b):
        if b[idx:idx+n] == a:
            result = 1
            break
 
 
    print(f'#{test_case} {result}')