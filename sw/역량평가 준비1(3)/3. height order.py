import sys

sys.stdin = open('sample_input3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]
    student_low = {i:[] for i in range(1,M+1)}
    student_low2 = {i:set() for i in range(1,M+1)}
    student_high = {i:[] for i in range(1,M+1)}
    student_high2 = {i:set() for i in range(1,M+1)}
    result = 0
    for a, b in arr:
        student_low[b].append(a)
        student_high[a].append(b)
    for i in range(1, N+1):
        stack = []
        visited = [0]*(N+1)
        if student_low[i]:
            stack.extend(student_low[i])
            student_low2[i].update(student_low[i])
            while stack:
                c = stack.pop()
                if visited[c] == 0:
                    visited[c] = 1
                    if not student_low[c]:
                        continue
                    stack.extend(student_low[c])
                    student_low2[i].update(student_low[c])
        stack = []
        visited = [0]*(N+1)
        if student_high[i]:
            stack.extend(student_high[i])
            student_high2[i].update(student_high[i])
            while stack:
                c = stack.pop()
                if visited[c] == 0:
                    visited[c] = 1
                    if not student_high[c]:
                        continue
                    stack.extend(student_high[c])
                    student_high2[i].update(student_high[c])
 
    for i in range(1, N+1):
        if len(student_low2[i]) + len(student_high2[i]) == N-1:
            result += 1
 
    print(f'#{tc} {result}')