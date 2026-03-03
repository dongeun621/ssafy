import sys

sys.stdin = open('sample_input20.txt', 'r')

from itertools import product, combinations
import copy
from collections import deque

def test(copy):
    for i in range(W): #W마다 테스트
        n = 1
        for j in range(1, D):
            if n == K: #이미 통과했으면 다 통과
                break
            if copy[j][i] == copy[j-1][i]: #같으면 +1
                n += 1
            else: n = 1 #다르면 다시 1로 복구
        if n == K:
            if i == W-1: # W까지 다 통과하면 result 반영
                global result
                result = True
                return
            else:continue # 테스트 통과했으면 다음 W
        else: break #하나라도 통과 못했으면 break (약쏘로 가야됨)


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    q = deque()
    result = False
    arr = [x for x in range(D)]

    for cnt in range(D+1):
        if cnt == 0: #0일때 따로 확인
            test(matrix)
            if result == True:
                break
            else: continue

        for D_list in combinations(arr, cnt): # 조합뽑아서 약 투여
            for madic in product([0,1], repeat=cnt): # 약넣을 D별 약 선택
                madic = list(madic)
                map_1 = [arr[:] for arr in matrix]  # 조합마다 copy 제공
                for d in D_list: # 약넣을 D번호 d
                    a = madic.pop()
                    map_1[d] = [a]*W
                test(map_1)
                if result == True:
                    break
            if result == True:
                break
        if result == True:
            break

    print(f'#{tc} {cnt}')