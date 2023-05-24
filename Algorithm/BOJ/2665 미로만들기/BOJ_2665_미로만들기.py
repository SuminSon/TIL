import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = (int)(input())
maze = [list(map(int,input().rstrip())) for _ in range(N)]
visit = [[10**8]*N for _ in range(N)]

q = deque([(0,0)])
visit[0][0] = 0
di, dj = [1,-1,0,0],[0,0,1,-1]
while q:
    i,j = q.popleft()
    if i==N-1 and j == N-1:
        print(visit[i][j])
        break
    for k in range(4):
        ii,jj = i + di[k], j+dj[k]
        if 0<=ii<N and 0<=jj<N:
            if maze[ii][jj] == 1: # 흰방. 가중치 0
                if visit[ii][jj] > visit[i][j]:
                    visit[ii][jj] = visit[i][j]
                    q.appendleft((ii,jj))
            else: # 검은방. 가중치 1
                if visit[ii][jj] > visit[i][j] + 1:
                    visit[ii][jj] = visit[i][j] + 1
                    q.append((ii,jj))