import sys

sys.stdin = open('sample_input15.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    n_dict = {}
    direct = [[0,1], [0,-1], [-1,0], [1,0]]

    for i, a in enumerate(arr):
        n_dict[i] = {}
        n_dict[i]['x'] = a[0]
        n_dict[i]['y'] = a[1]
        n_dict[i]['direct'] = a[2]
        n_dict[i]['k'] = a[3]

    print(n_dict)
