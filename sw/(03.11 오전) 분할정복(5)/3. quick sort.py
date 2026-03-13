import sys

sys.stdin = open('sample_input3.txt', 'r')

def quicksort(arr, left, right):
    if left >= right:
        return
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    pivot_idx = i + 1
    quicksort(arr, left, pivot_idx - 1)
    quicksort(arr, pivot_idx + 1, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')