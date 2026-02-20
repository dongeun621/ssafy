import sys

sys.stdin = open('sample_input7.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    floors = list(map(int, input().split()))
    result = 0
    for a in range(2, N-2):
        best = 0
        break_signal = 0
        for b in range(a-2, a+3):
            if a == b:
                continue
            elif floors[a] <= floors[b]:
                break_signal = 1
                break
            elif best <= floors[b] and floors[a] != floors[b]:
                best = floors[b]
        if break_signal == 0:
            result += floors[a]-best
 
    print(f'#{test_case} {result}')