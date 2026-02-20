import sys

sys.stdin = open('sample_input6.txt', 'r')

T = 10
for test_case in range(1, T+1):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    i = 1
    j = 100 - (matrix[-1].index(2))
    direc = 's'
    #위, 좌, 우
    # [1, 0], [0, 1], [0, -1]
    while i != 100:
        S = matrix[-(i + 1)][-j]
        if j == 1:
            L = matrix[-i][-(j + 1)]
            R = 0
        elif j == 100:
            L = 0
            R = matrix[-i][-(j - 1)]
        else:
            L = matrix[-i][-(j + 1)]
            R = matrix[-i][-(j - 1)]
 
        if direc == 's':
            if L == 1:
                j += 1
                direc = 'l'
            elif R == 1:
                j += -1
                direc = 'r'
            else:
                i += 1
        elif direc == 'l':
            if L == 1:
                j += 1
            else:
                i += 1
                direc = 's'
        elif direc == 'r':
            if R == 1:
                j += -1
            else:
                i += 1
                direc = 's'
    result = 100 - j
 
    print(f'#{test_case} {result}')