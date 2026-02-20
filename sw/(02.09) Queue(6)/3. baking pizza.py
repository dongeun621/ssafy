import sys

sys.stdin = open('sample_input3.txt', 'r')

from collections import deque
 
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pizza = deque(map(int, input().split()))
    fire = deque()
    cnt = 1
 
    while len(fire) != 1 or len(pizza) != 0:
        if len(fire) < N and len(pizza) > 0:
            fire.appendleft([pizza.popleft(), cnt])
            cnt += 1
        else:
            fire.rotate(1)
            fire[0][0] //= 2
            if fire[0][0] == 0:
                fire.popleft()
 
 
    print(f'#{test_case} {fire[0][1]}')