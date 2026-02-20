import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    result = ['.', '.', '#', '.', '.']
    word = list(input())
    for a in word:
        for i in range(5):
            if i == 0 or i == 4:
                result[i] += '.#..'
            elif i == 1 or i == 3:
                result[i] += '#.#.'
            elif i == 2:
                result[i] += '.'
                result[i] += a
                result[i] += '.#'
    for i in result:
        print(i)