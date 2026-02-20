import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = [0, 0]
    for i in arr:
        result_list[i] += 1
    for i in range(len(result_list)):
        if result[1] <= result_list[i]:
            result = [i, result_list[i]]
    print(f'#{test_case} {result[0]} {result[1]}')