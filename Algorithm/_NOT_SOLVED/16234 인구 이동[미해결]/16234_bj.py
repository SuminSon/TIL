# 16234 인구 이동

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx, dy = [1,-1,0,0],[0,0,-1,1]

def bfs(s:(int,int)):
    global group_num, is_moved
    q = deque([s])
    while q:
        x, y = q.popleft()
        for k in range(4):
            dxx, dyy = x + dx[k], y + dy[k]
            # 국경선 개방
            if 0 <= dxx < N and 0 <= dyy < N and L <= abs(A[dxx][dyy]-A[x][y]) <= R and visited[dxx][dyy] == 0:
                is_moved = True
                if visited[x][y] == 0:
                    visited[x][y] = group_num
                    group_population[group_num] += A[x][y]
                    group_block[group_num] += 1
                visited[dxx][dyy] = group_num
                group_population[group_num] += A[dxx][dyy]
                group_block[group_num] += 1
                q.append((dxx,dyy))
    group_num += 1
    group_population.append(0)
    group_block.append(0)

N, L, R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

is_moved = True
Day = 0

while is_moved:
    is_moved = False

    group_population = [0,0]
    group_block = [0,0]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    group_num = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs((i,j))

    if is_moved:
        for i in range(N):
            for j in range(N):
                for gn in range(1, group_num):
                    if visited[i][j] == gn:
                        A[i][j] = group_population[gn] // group_block[gn]

        Day += 1

print(Day)