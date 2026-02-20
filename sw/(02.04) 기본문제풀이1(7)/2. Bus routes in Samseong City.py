import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    J = [int(input()) for _ in range(P)]
    bus_stop = [0]*5001
 
    for i in range(N):
        for j in range(bus[i][0], bus[i][1]+1):
            bus_stop[j] += 1
    print(f'#{test_case}', end=' ')
 
    for index, i in enumerate(J):
        if index == P-1:
            print(bus_stop[i])
            break
        print(bus_stop[i], end=' ')