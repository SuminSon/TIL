# 7576 백준 토마토

import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(q):
    global arr
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 1
    while q:
        v = q.popleft()
        x,y = v[0], v[1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))
                cnt = arr[nx][ny]

    if all(0 not in t for t in arr):
        return cnt-1
    else:
        return -1

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i,j))

print(bfs(q))