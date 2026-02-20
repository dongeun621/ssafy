import sys

sys.stdin = open('sample_input1.txt', 'r')

from itertools import combinations, permutations
T = int(input())
for tc in range(1, 1+T):
    arr1 = list(input())
    arr = []
    result = False
    for i in arr1:
        arr.append(int(i))
    for i in combinations([0,1,2,3,4,5], 3):
        first_run = 0
        first_triplet = 0


    print(result)