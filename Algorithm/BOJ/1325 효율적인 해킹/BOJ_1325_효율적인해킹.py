import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(i):
    global max_cnt_hack, max_hack_com
    q = deque([i])
    visited = [0 for _ in range(N + 1)]
    visited[i] = 1
    cnt_hack = 1
    while q:
        v = q.popleft()
        for w in com_hack[v]:
            if visited[w] == 0:
                cnt_hack += 1
                visited[w] = 1
                q.append(w)

    if max_cnt_hack < cnt_hack:
        max_cnt_hack = cnt_hack
        max_hack_com = [i]
    elif max_cnt_hack == cnt_hack:
        max_hack_com.append(i)

N, M = map(int,input().split())

com_hack = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    com_hack[B].append(A)

max_cnt_hack = 0
max_hack_com = []

for i in range(1,N+1):
    bfs(i)

for m in max_hack_com:
    print(m,end=' ')
print()
