import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx,dy = [-1,1,0,0],[0,0,-1,1]

# 13460 구슬 탈출 2
X, Y = map(int,input().split())
map = [list(input().strip()) for _ in range(X)]
# rx ry bx by의 현재 위치 상태 메모
visited = [[[[False]*Y for _ in range(X)] for _ in range(Y)] for _ in range(X)]
q = deque()
rx, ry, bx, by = [0] * 4

def init():
    rx, ry, bx, by = [0] * 4
    count = 0
    isR = isB = False
    for i in range(X):
        for j in range(Y):
            if map[i][j] == 'R':
                rx,ry = i,j
                isR = True
            elif map[i][j] == 'B':
                bx,by = i,j
                isB = True
            if isR and isB: break
        if isR and isB: break
    visited[rx][ry][bx][by] = True
    q.append((rx,ry,bx,by,count))

def bfs():
    init()
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count >= 10: continue;
        for k in range(4):
            nrx, nry, nbx, nby = [0] *4
            r_stop = b_stop = False
            isSuccess = isFail = False
            # 두 구슬 전부 멈출 때까지 한 칸씩 직진
            i = 1
            while True:
                rxx = rx + dx[k] * i
                ryy = ry + dy[k] * i
                bxx = bx + dx[k] * i
                byy = by + dy[k] * i
                # 파란 공이 먼저 들어가면 실패
                if (not b_stop) and (map[bxx][byy] == 'O'):
                    isFail = True
                    break
                # 빨간 공이 들어가면 성공
                if (not r_stop) and (map[rxx][ryy] == 'O'):
                    isSuccess = True
                # 벽을 만나면 한 칸 뒤로 와서 멈추기
                if (not b_stop) and (map[bxx][byy] == '#'):
                    nbx = bxx - dx[k]
                    nby = byy - dy[k]
                    b_stop = True
                # 벽을 만나면 한 칸 뒤로 와서 멈추기
                if (not r_stop) and (map[rxx][ryy] == '#'):
                    nrx = rxx - dx[k]
                    nry = ryy - dy[k]
                    r_stop = True
                # 같은 곳에 있을 수 없으니 나중에 온 구슬을 한칸 뒤로
                # bxx byy 파란 구슬의 다음 위치 nrx nry 빨간 구슬의 현재 위치
                if (not b_stop and bxx == nrx and byy == nry):
                    nbx = bxx - dx[k]
                    nby = byy - dy[k]
                    b_stop = True
                # 같은 곳에 있을 수 없으니 나중에 온 구슬을 한칸 뒤로
                # bxx byy 파란 구슬의 다음 위치 nrx nry 빨간 구슬의 현재 위치
                if (not r_stop and rxx == nbx and ryy == nby):
                    nrx = rxx - dx[k]
                    nry = ryy - dy[k]
                    r_stop = True
                # 둘 다 멈췄다면 직진 종료
                if r_stop and b_stop:
                    break
                i += 1
            if isFail: continue
            if isSuccess:
                print(count + 1)
                return 0
            if (visited[nrx][nry][nbx][nby] == False):
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,count + 1))
    print(-1)

bfs()

