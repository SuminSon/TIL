# 16234 인구이동 2차도전

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = [1,-1,0,0],[0,0,-1,1]

def bfs(s:(int,int)):
    q = deque([s])
    while q:
        x, y = q.popleft()
        for k in range(4):
            dxx, dyy = x + dx[k], y + dy[k]
            if 0 <= dxx < N and 0 <= dyy < N and L <= abs(A[dxx][dyy]-A[x][y]) <= R and visited[dxx][dyy] == 0 :
                if visited[x][y] == 0:
                    visited[x][y] = 1
                    group_idxs.append((x,y))





N, L, R = map(int,input().split())
A = [ list(map(int,input().split())) for _ in range(N) ]
visited = [ [0 for _ in range(N)] for _ in range(N) ]
group_idxs = []
group_popu = 0
group_block = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs((i,j))