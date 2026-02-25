import sys

sys.stdin = open('sample_input3.txt', 'r')

def pick(left, right, i):
    global result
    if i == []:
        result += 1
        return
    pick(left+i[0],right,i[1:])
    if left >= right + i[0]:
        pick(left, right + i[0], i[1:])
    else: return


from itertools import permutations, combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in permutations(arr):
        i = list(i)
        pick(0,0,i)

    print(f'#{tc} {result}')