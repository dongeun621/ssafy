import sys

sys.stdin = open('sample_input15.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    n_dict = {}
    direct = [[0,1], [0,-1], [-1,0], [1,0]]
    result = 0

    for i, a in enumerate(arr):
        n_dict[i] = {
            'x': a[0]*2,
            'y': a[1]*2,
            'direct': a[2],
            'k': a[3]
        }


    for _ in range(4000):
        temp_dict = {}
        for i, n in n_dict.items():
            n['x'] += direct[n['direct']][0]
            n['y'] += direct[n['direct']][1]
            x = n['x']
            y = n['y']
            if (x, y) not in temp_dict:
                temp_dict[(x, y)] = []
            temp_dict[(x, y)].append(i)

        for n in temp_dict:
            if len(temp_dict[n]) > 1:
                for i in temp_dict[n]:
                    result += n_dict[i]['k']
                    n_dict.pop(i)


    print(f'#{tc} {result}')
