import sys

sys.stdin = open('sample_input5.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = input().split()
    arr = list(N)
    N = len(arr)
    K = int(K)
    result_set = [[] for _ in range(K+1)]
    result_set[0].append(arr)
    result = 0
    for k in range(1, K+1):
        for one_arr in result_set[k - 1]:
            for i in range(N):
                for j in range(i+1, N):
                    temp = one_arr[:]
                    a = temp[i]
                    b = temp[j]
                    temp[i] = b
                    temp[j] = a
                    if temp not in result_set[k]:
                        result_set[k].append(temp)
    for arr_list in result_set[K]:
        num = 0
        for a in arr_list:
            num *= 10
            num += int(a)
        result = max(result, num)

    print(f"#{tc} {result}")
