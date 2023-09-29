import sys
from collections import deque
sys.stdin = open('input.txt')

# 3% 시간초과

R,C = map(int,input().split())

cave = [list((str)(input())) for _ in range(R)]
N = (int)(input())

# True == left, False == right
dir = True

def cluster_bfs(x,y):
    global cave
    visited = [[False] * C for _ in range(R)]
    q = deque([(x,y)])
    cluster = [(x,y)]
    visited[x][y] = True

    while q:
        i,j = q.popleft()
        if i == R-1:
            return

        for k in [(0,-1),(0,1),(-1,0),(1,0)]:
            di,dj = k
            ni, nj = i + di , j + dj
            if 0 <= ni < R and 0 <= nj < C and cave[ni][nj] == 'x' and visited[ni][nj] == False:
                q.append((ni,nj))
                cluster.append((ni, nj))
                visited[ni][nj] = True

    minK = R + 1
    for c in cluster:
        ci,cj = c
        k = 0
        while ci+1 < R and (cave[ci+1][cj] == '.' or (ci+1,cj) in cluster):
                k += 1
                ci += 1
        minK = min(minK, k)

    if 0 < minK:
        cluster.sort(key=lambda x:x[0],reverse=True)

        for c in cluster:
            ci,cj = c
            cave[ci][cj] = '.'
            cave[ci + minK][cj] = 'x'

hs = map(int,input().split())
for h in hs:
    hr = R - h

    # 왼쪽에서 쏘기
    if dir:
        for c in range(C):
            if cave[hr][c] == 'x':
                cave[hr][c] = '.'

                # 여기서부터 왼오위아래 탐색해서 다른 클러스터 파악
                for d in [(0,-1),(0,1),(-1,0),(1,0)]:
                    di, dj = d
                    ni, nj = hr + di, c + dj
                    # 클러스터 발견
                    if 0 <= ni < R and 0 <= nj < C and cave[ni][nj] == 'x':
                        cluster_bfs(ni,nj)
                break

    # 오른쪽에서 쏘기
    else:
        for c in range(C-1,-1,-1):
            if cave[hr][c] == 'x':
                cave[hr][c] = '.'

                # 여기서부터 왼오위 탐색해서 다른 클러스터 파악
                for d in [(0,-1),(0,1),(-1,0),(1,0)]:
                    di, dj = d
                    ni, nj = hr + di, c + dj
                    # 클러스터 발견
                    if 0 <= ni < R and 0 <= nj < C and cave[ni][nj] == 'x':
                        cluster_bfs(ni, nj)
                break

    dir = not dir

for r in range(R):
    for c in range(C):
        print(cave[r][c], end='')
    print()