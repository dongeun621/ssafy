import sys

sys.stdin = open('sample_input1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = {}
    complete = []

    for i in range(1, N+1):
        graph[i] = arr[i-1][1:]
        if graph[i] == []:
            complete.append(i)

    result = 1

    while len(complete) < N:
        temp_complete = []
        for i in range(1, N+1):
            if i not in complete: #완료하지 않았고
                temp_complete.append(i) #일단 완료에 넣고
                for need_subject in graph[i]:
                    if need_subject not in complete: #필요과목이 완료과목에 없으면 빼기
                        temp_complete.pop()
                        break
        if temp_complete == []: #추가된 과목없으면 -1
            result = -1
            break
        complete.extend(temp_complete)
        result += 1

    print(f'#{tc} {result}')