import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, W1, W2 = map(int, input().split())
    W_list = list(map(int, input().split()))
    W_list.sort(reverse=True)
    w1 = []
    w2 = []
    result = 0
    for i in W_list:
        if len(w1) < W1:
            if len(w1) == len(w2):
                w1.append(i)
                result += i*len(w1)
            elif len(w2) < W2:
                w2.append(i)
                result += i*len(w2)
            else:
                w1.append(i)
                result += i*len(w1)
        else:
            w2.append(i)
            result += i * len(w2)
    print(f'#{tc} {result}')