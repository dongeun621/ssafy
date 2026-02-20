import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = 1
 
    for i in range(9):
        if result == 0:
            break
        check_list = [0]*9
        for j in range(9):
            check_list[matrix[i][j]-1] += 1
        for k in check_list:
            if k != 1:
                result = 0
                break
 
    for i in range(9):
        if result == 0:
            break
        check_list = [0]*9
        for j in range(9):
            check_list[matrix[j][i]-1] += 1
        for k in check_list:
            if k != 1:
                result = 0
                break
 
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if result == 0:
                break
            check_list = [0] * 9
            for a in range(i, i+3):
                for b in range(j, j+3):
                    check_list[matrix[a][b] - 1] += 1
            for k in check_list:
                if k != 1:
                    result = 0
                    break

 
    print(f'#{test_case} {result}')