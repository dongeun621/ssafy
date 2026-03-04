import sys

sys.stdin = open('sample_input1.txt', 'r')

def before(i):
    before_arr.append(i)
    length = len(arr[i])
    if length > 0:
        before(arr[i][0])
    if length > 1:
        before(arr[i][1])

def middle(i):
    length = len(arr[i])
    if length > 0:
        middle(arr[i][0])
    middle_arr.append(i)
    if length > 1:
        middle(arr[i][1])

def after(i):
    length = len(arr[i])
    if length > 0:
        after(arr[i][0])
    if length > 1:
        after(arr[i][1])
    after_arr.append(i)


V = int(input())
tree = list(map(int,input().split()))
arr = [[] for _ in range(V+1)]

for i in range(0,24,2):
    arr[tree[i]].append(tree[i+1])

before_arr = []
middle_arr = []
after_arr = []

before(1)
middle(1)
after(1)

print(*before_arr)
print(*middle_arr)
print(*after_arr)