import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_list = [list(map(int, input().split())) for _ in range(N)]
    n_list.sort(key=lambda x:x[1])
    result = 0
    end = 0
    for i in range(N):
        min_end = 25
        for a, b in n_list:
            if a >= end:
                min_end = min(min_end, b)
        if min_end == 25:
            break
        end = min_end
        result += 1
 
 
 
    print(f'#{test_case} {result}')