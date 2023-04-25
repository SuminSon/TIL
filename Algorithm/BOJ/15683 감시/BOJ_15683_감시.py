import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')

def cctv_set(num = 1):
    global min_blind_spot, area, cctvs

    if num-1 == len(cctvs):
        blind_spot = 0
        for n in range(len(area)):
            blind_spot += area[n].count(0)
        if blind_spot < min_blind_spot:
            min_blind_spot = blind_spot
        return

    x, y , k = cctvs[num-1]
    for kk in range(0, len(dx[k])):
        if not type(dx[k][kk]) is int:
            for kkk in range(0, len(dx[k][kk])):
                for a in range(1, max(N, M)):
                    dxx, dyy = x + dx[k][kk][kkk] * a, y + dy[k][kk][kkk] * a
                    if 0 <= dxx < N and 0 <= dyy < M and arr[dxx][dyy] != 6 and area[dxx][dyy] == 0:
                        area[dxx][dyy] = num
                    elif not (0 <= dxx < N and 0 <= dyy < M) or arr[dxx][dyy] == 6:
                        break
            cctv_set(num +1)
            for kkk in range(0, len(dx[k][kk])):
                for a in range(1, max(N, M)):
                    dxx, dyy = x + dx[k][kk][kkk] * a, y + dy[k][kk][kkk] * a
                    if 0 <= dxx < N and 0 <= dyy < M and arr[dxx][dyy] != 6 and area[dxx][dyy] == num:
                        area[dxx][dyy] = 0
                    elif not (0 <= dxx < N and 0 <= dyy < M) or arr[dxx][dyy] == 6:
                        break
        else:
            for a in range(1, max(N, M)):
                dxx, dyy = x + dx[k][kk] * a, y + dy[k][kk] * a
                if 0 <= dxx < N and 0 <= dyy < M and arr[dxx][dyy] != 6 and area[dxx][dyy] == 0:
                    area[dxx][dyy] = num
                elif not(0 <= dxx < N and 0 <= dyy < M) or arr[dxx][dyy] == 6:
                    break
            cctv_set(num + 1)
            for a in range(1, max(N, M)):
                dxx, dyy = x + dx[k][kk] * a, y + dy[k][kk] * a
                if 0 <= dxx < N and 0 <= dyy < M and arr[dxx][dyy] != 6 and area[dxx][dyy] == num:
                    area[dxx][dyy] = 0
                elif not(0 <= dxx < N and 0 <= dyy < M) or arr[dxx][dyy] == 6:
                    break

# N : 세로, M : 가로
N, M = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(N) ]

# 1 ~ 5
dx = [[],[(0),(0),(1),(-1)],[(0,0),(-1,1)],[(1,0),(-1,0),(1,0),(-1,0)],[(0,0,1),(0,0,-1),(0,1,-1),(0,1,-1)],[(0,0,1,-1)]]
dy = [[],[(1),(-1),(0),(0)],[(-1,1),(0,0)],[(0,1),(0,-1),(0,-1),(0,1)],[(1,-1,0),(1,-1,0),(1,0,0),(-1,0,0)],[(1,-1,0,0)]]
min_blind_spot = 10 ** 8
cctvs = []
area = [ [0 for _ in range(M)] for _ in range(N) ]
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctvs.append((i,j,arr[i][j]))
            area[i][j] = -1
        elif arr[i][j] == 6:
            area[i][j] = -1

cctv_set(1)
print(min_blind_spot)
