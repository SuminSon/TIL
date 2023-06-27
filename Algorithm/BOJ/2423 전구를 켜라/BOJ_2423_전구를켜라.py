import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 세로 M 가로
N, M = map(int,input().split())
board = [list(map(lambda x:1 if x=="/" else 0, input().rstrip())) for _ in range(N)]
di, dj = [1,1,-1,-1],[1,-1,-1,1]

def BFS01():
    # 2배수가 되지 않으면 시작점에서 (N,M)에 도달할 수 없음
    if (N+M)%2:
        return "NO SOLUTION"


    visit = [[0]*(M+1) for _ in range(N+1)]
    visit[0][0] = 0
    q = deque([(0,0,0)])
    while q:
        c,i,j = q.popleft()

        # 방문 했다면 PASS
        if visit[i][j]:
            continue
        visit[i][j] = 1

        # 목적지에 도착했다면 최소 횟수리턴
        if i == N and j == M:
            return c

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<=N and 0<=nj<=M and not visit[ni][nj]:
                if k==0:
                    if board[i][j] == 0:
                        q.appendleft((c, ni, nj))
                    else:
                        q.append((c+1,ni,nj))
                elif k==1:
                    if board[i][j-1] == 1:
                        q.appendleft((c, ni, nj))
                    else:
                        q.append((c+1,ni,nj))
                elif k==2:
                    if board[i-1][j-1] == 0:
                        q.appendleft((c, ni, nj))
                    else:
                        q.append((c+1,ni,nj))
                else:
                    if board[i-1][j] == 1:
                        q.appendleft((c, ni, nj))
                    else:
                        q.append((c+1,ni,nj))

print(BFS01())
