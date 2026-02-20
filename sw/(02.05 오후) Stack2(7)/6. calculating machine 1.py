import sys

sys.stdin = open('sample_input6.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = input()
    arr = list(map(int, input().split('+')))
    print(f'#{test_case} {sum(arr)}')