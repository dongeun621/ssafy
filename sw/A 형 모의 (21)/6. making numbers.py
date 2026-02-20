import sys

sys.stdin = open('sample_input6.txt', 'r')

def pernutat(l, m):
    for i in range(4):
        if m[i] > 0:
            l.append(i)
            m[i] -= 1
            pernutat(l, m)
            l.pop()
            m[i] += 1
    if len(l) == N-1:
        M_per.append(l[:])
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # M: 연산자들
    M = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    M_per = []
 
    pernutat([], M)
 
 
    max_result = 'False'
    min_result = 'False'
    for M_per_inner in M_per:
        result = N_list[0]
        for i in range(N-1):
            if M_per_inner[i] == 0:
                result += N_list[i + 1]
            elif M_per_inner[i] == 1:
                result -= N_list[i + 1]
            elif M_per_inner[i] == 2:
                result *= N_list[i + 1]
            elif M_per_inner[i] == 3:
                if result < 0:
                    result = result * (-1)
                    result //= N_list[i + 1]
                    result = result * (-1)
                else:
                    result //= N_list[i + 1]
        if min_result == 'False':
            min_result = result
        else: min_result = min(min_result, result)
        if max_result == 'False':
            max_result = result
        else: max_result = max(max_result, result)
    print(f'#{tc} {max_result-min_result}')