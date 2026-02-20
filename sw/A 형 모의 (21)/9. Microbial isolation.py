import sys

sys.stdin = open('sample_input8.txt', 'r')

dxy = [0, [-1,0], [1,0], [0,-1], [0,1]]
reverse = [0, 2, 1, 4, 3]
 
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    for _ in range(M):
        dic = {}
        for i, j, n, dir in arr:
            i += dxy[dir][0]
            j += dxy[dir][1]
 
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                n //= 2
                dir = reverse[dir]
 
            if (i,j) in dic:
                dic[(i,j)][0] += n
                if dic[(i,j)][1] < n:
                    dic[(i, j)][1] = n
                    dic[(i, j)][2] = dir
            else:
                dic[(i,j)] = [n, n, dir]
 
        arr = [[i,j,n,dir] for (i,j), [n, nn, dir] in dic.items()]
    result = sum(i[2] for i in arr)
 
    print(f'#{tc} {result}')