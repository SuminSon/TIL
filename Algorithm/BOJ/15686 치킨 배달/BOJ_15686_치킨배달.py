import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 집에서부터 시작해서 치킨집까지의 거리를 chicken_dist에 갱신
# (치킨집 좌표) : [집1에서의 치킨거리, 집2에서의 치킨거리...]
def bfs(s:(int,int)):
    q = deque()
    q.append(s)
    visited = [[0 for _ in range(N)] for _ in range(N) ]
    while q:
        v = q.popleft()
        x, y = v

        if arr[x][y] == 2:
            if (x,y) not in chicken_dist:
                chicken_dist[(x,y)] = [visited[x][y]]
            else:
                chicken_dist[(x,y)].append(visited[x][y])

        for d in range(4):
            dxx, dyy = x + dx[d], y + dy[d]
            if 0<=dxx<N and 0<=dyy<N and visited[dxx][dyy] == 0:
                visited[dxx][dyy] = visited[x][y] + 1
                q.append((dxx,dyy))

# K개의 치킨집 중 M개의 치킨집을 고르는 순열
# 고른 치킨집들에서의 도시 최소 치킨거리를 구해 city_cd 리스트에 갱신
# 이후 city_cd에서의 최솟값을 구해 출력할 것
def kPm(K:int, M:int, idx=0, elem=[]):
    if M==0 :
        #print('조합값',elem)

        all_min = 0
        for h in range(H):
            h_min = 10**8
            for e in elem:
                if chicken_dist[e][h] < h_min:
                    h_min = chicken_dist[e][h]

            all_min += h_min
        city_cd.append(all_min)

        return

    for c in range(idx,K):
        if chicken_xy[c] not in elem:
            kPm(K, M-1, c, elem+[chicken_xy[c]])


N, M =map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chicken_dist = {}
chicken_xy = []
H = 0 # 집 개수

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs((i,j))
            H += 1
        elif arr[i][j] == 2:
            chicken_xy.append((i,j))

#print(chicken_dist)
#print(chicken_xy)
#print(len(chicken_dist))
#print(H)
city_cd = []
K = len(chicken_dist)
kPm(K, M)
#print(city_cd)
print(min(city_cd))