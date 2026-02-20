import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, Q = map(int, input().split())
    result = []
    for i in range(N):
        result.append(0)
    for a in range(Q):
        L, R = map(int, input().split())
        for b in range(L-1,R):
            result[b] = a+1
    print(f'#{test_case}', end=' ')
    print(*result)