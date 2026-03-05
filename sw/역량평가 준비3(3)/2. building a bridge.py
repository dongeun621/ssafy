import sys

sys.stdin = open('sample_input2.txt', 'r')

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

from itertools import combinations
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
island = []
island_idx = 0
graph = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1: #섬 찾으면(2로 바뀌지않은 새로운)
            stack = [[i,j]] #스택에 넣어서
            matrix[i][j] = 2
            island.append([])
            while stack: #섬크기 파악
                x, y = stack.pop()
                island[island_idx].append([x,y]) #인덱스에 해당하는 섬번호에 넣음
                for dx, dy in dxy:
                    xx = x + dx
                    yy = y + dy
                    if 0 <= xx < N and 0 <= yy < M and matrix[xx][yy] == 1:
                        matrix[xx][yy] = 2  # 방문하면 2로 바꿈
                        stack.append([xx, yy])
            island_idx += 1
r = len(island)
for A,B in combinations(range(r), 2): #다리 연결할 섬조합
    min_dic = 10
    for ax, ay in island[A]: #각 섬의 한 부분 추출
        for bx, by in island[B]:
            if ax == bx: # x가 같을때
                if ay > by: #어디의 y가 더 높은지
                    max_y = ay
                    min_y = by + 1
                else:
                    max_y = by
                    min_y = ay + 1
                if sum(matrix[ax][min_y:max_y]) == 0 and max_y - min_y >= 2:  # 해당 x에서 두 섬사이에 아무것도 없는지, 다리길이 2보다 큰지
                    min_dic = min(min_dic, max_y - min_y)

            elif ay == by:
                if ax > bx:
                    max_x = ax
                    min_x = bx + 1
                else:
                    max_x = bx
                    min_x = ax + 1
                if sum(matrix[x][ay] for x in range(min_x, max_x)) == 0 and max_x-min_x >= 2: #해당 y에서 두 섬사이에 아무것도 없는지, 다리길이 2보다 큰지
                    min_dic = min(min_dic, max_x-min_x)
    if min_dic != 10:# min_dic가 바꼈으면 그래프에 추가
        graph.append([A, B, min_dic])

def connet(a,b):
    visited = [a]
    stack = [a]
    while stack:
        next_list = graph2[stack.pop()]
        for next in next_list:
            if next == b:
                return True
            if next not in visited:
                stack.append(next)
                visited.append(next)
    return False

result = 0
graph2 = [[] for _ in range(r)]
if len(graph) >= r-1:
    graph.sort(key=lambda x: x[2])
    cnt = 0
    for a, b, d in graph:
        if connet(a,b) == False:
            graph2[a].append(b)
            graph2[b].append(a)
            result += d
            cnt += 1
    if cnt < r - 1:
        result = -1

else:
    result = -1
print(result)

