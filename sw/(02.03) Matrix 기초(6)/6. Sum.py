import sys

sys.stdin = open('sample_input6.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []
    for i in matrix:
        sum_list.append(sum(i))
    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += matrix[j][i]
        sum_list.append(sum1)
    sum2 = 0
    for i in range(100):
        sum2 += matrix[i][i]
    sum_list.append(sum2)
 
    result = max(sum_list)
 
 
    print(f'#{test_case} {result}')