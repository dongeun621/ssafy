import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = None
    M -= 1
    for k in range(N):
        if k == 0: #0일땐 한번만
            start_list = [M]
        else: #나머진 양쪽으로 두번
            start_list = [M-k, M+k]

        for start in start_list:
            temp_arr = arr[:]
            bomb = 0
            while sum(temp_arr) != 0:
                near_target = [N,N] #[인덱스번호, start와의 거리]
                for target in range(N):
                    if temp_arr[target] == 1:# 보석이 있는 칸인지
                        delta = abs(start-target)
                        if near_target[1] > delta:# 기존보다 더 가까운지
                            near_target = [target, delta]
                            bomb = 0# 최신화됐을땐 0으로 바꿔줌
                        elif near_target[1] == delta:# 기존이랑 같으면 1
                            bomb = 1
                if bomb == 1:
                    break
                start = near_target[0] #가장 가까운 인덱스를 다음 스타트로
                temp_arr[start] = 0 #다음 스타트는 보석회수해서 0
            if sum(temp_arr) == 0: #성공하면 k 를 결과로
                result = k
                break
        if result != None:
            break

    print(f'#{tc} {result}')


