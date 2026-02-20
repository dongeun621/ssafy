import sys

sys.stdin = open('sample_input7.txt', 'r')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 100
    left_box = N
    break_signal = 0
    for i in range(100, 0, -1):
        for a in arr:
            if a >= i:
                left_box -= 1
        if left_box < 0:
            break
        result -= 1
    left_box = N
    break_signal = 0
 
    for i in range(100):
        for a in arr:
            if a <= i:
                left_box -= 1
        if left_box < 0:
            break
        result -= 1
    if result < 0:
        result = 0
 
    print(f'#{test_case} {result}')