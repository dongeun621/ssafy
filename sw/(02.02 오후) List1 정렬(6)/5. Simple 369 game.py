import sys

sys.stdin = open('sample_input5.txt', 'r')

N = int(input())
 
for i in range(1, N+1):
    nlist = list(map(int, str(i)))
    count = 0
    for j in nlist:
        if j == 3 or j == 6 or j == 9:
            count += 1
    if count == 0:
        print(i, end= ' ')
    else:
        print('-'*count, end=' ')