import sys

sys.stdin = open('sample_input17.txt', 'r')

direct = [[0,0], [0,-1], [1,0], [0,1], [-1,0]]

T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(N)]
    bc = {}
    a = [1,1]
    b = [10,10]
    for i in BC:
        bc[(i[0],i[1])] = {'range': i[2], 'power': i[3]}
    result = 0
    for t in range(-1, M):
        if t != -1:
            a[0] += direct[A[t]][0]
            a[1] += direct[A[t]][1]
            b[0] += direct[B[t]][0]
            b[1] += direct[B[t]][1]
        A_bc = []
        B_bc = []
        for x,y in bc:
            a_dxy = abs(x-a[0])+abs(y-a[1])
            b_dxy = abs(x-b[0])+abs(y-b[1])
            if bc[(x,y)]['range'] >= a_dxy:
                A_bc.append((x,y))
            if bc[(x,y)]['range'] >= b_dxy:
                B_bc.append((x,y))
        best_sum = 0
        if A_bc and B_bc:
            for a_bc in A_bc:
                for b_bc in B_bc:
                    if a_bc == b_bc:
                        best_sum = max(best_sum, bc[a_bc]['power'])
                    else:
                        best_sum = max(best_sum, bc[a_bc]['power']+bc[b_bc]['power'])
        elif A_bc:
            for a_bc in A_bc:
                best_sum = max(best_sum, bc[a_bc]['power'])
        elif B_bc:
            for b_bc in B_bc:
                best_sum = max(best_sum, bc[b_bc]['power'])
        result += best_sum
    print(f'#{tc} {result}')