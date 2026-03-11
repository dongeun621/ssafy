import sys

sys.stdin = open('sample_input2.txt', 'r')

dxy = [(0,1), (0,-1), (-1,0), (1,0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [tuple(map(int, input().split())) for _ in range(N)]
    dic = {}
    result = 0
    for i in range(N):
        x, y, direct, k = matrix[i]
        dic[(x*2, y*2)] = [direct, k]

    for ii in range(4000):
        temp_dic = {}
        bomb_list = []
        for (x,y), [direct, k] in dic.items():
            x += dxy[direct][0]
            y += dxy[direct][1]
            if (x,y) in temp_dic:
                bomb_list = [(x,y)]
                temp_dic[(x,y)].append(k)
            else:
                temp_dic[(x, y)] = [direct, k]

        for x,y in bomb_list:
            result += sum(temp_dic[(x,y)][1:])
            del temp_dic[(x,y)]
        dic = temp_dic.copy()

    print(f'#{tc} {result}')