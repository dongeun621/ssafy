import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    con_list = list(map(int, input().split()))
    truck_list = list(map(int, input().split()))
    con_list.sort()
    truck_list.sort()
    result = 0
    for _ in range(N):
        if truck_list:
            if con_list[-1] <= truck_list[-1]:
                result += con_list[-1]
                truck_list.pop()
        else: break
        con_list.pop()
 
    print(f'#{test_case} {result}')