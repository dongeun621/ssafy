import sys

sys.stdin = open('sample_input2.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    double_N = 2*N
    star_arr = list(map(int, input().split()))
    change_arr = []
    arr_sum = sum(star_arr)
    result = 0

    if arr_sum < double_N:
        for i in range(N):
            change_arr.append(max(star_arr[i]+i+1, i+1)-star_arr[i])
        change_arr.sort(reverse=True)

        for i in range(N):
            arr_sum += change_arr[i]
            result += 1
            if arr_sum >= double_N:
                break

    print(f'#{tc} {result}')