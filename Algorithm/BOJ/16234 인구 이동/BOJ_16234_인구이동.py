# 16234 인구이동 BFS

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

di, dj = [1,-1,0,0],[0,0,-1,1]

N,L,R = map(int,input().split())
cMap = [list(map(int,input().split())) for _ in range(N)]

def Solution():
    days = 0;
    while True:
        # 현 시점의 연합 수를 카운트
        unionNum = 0
        # 인구수, 칸 개수
        unionPtoC = [[0, 0] for _ in range(N * N)]
        # 연합 넘버 기록용 맵
        vMap = [[0] * N for _ in range(N)]
        # 1. 국경선 공유하는 두 나라 인구 차이가 L명 이상 R명 이하라면 국경선 open. 다 열리면 인구이동 start
        for i in range(N):
            for j in range(N):
                if vMap[i][j] == 0:
                    unionNum += 1
                    vMap[i][j] = unionNum
                    q = deque([(i,j)])
                    while q:
                        ti,tj = q.popleft()
                        unionPtoC[unionNum - 1][0] += cMap[ti][tj]
                        unionPtoC[unionNum - 1][1] += 1
                        for k in range(4):
                            ni,nj = ti +di[k], tj+dj[k]
                            if 0<=ni<N and 0<=nj<N and L <= abs(cMap[ti][tj] - cMap[ni][nj]) <= R and vMap[ni][nj] == 0:
                                vMap[ni][nj] = vMap[ti][tj]
                                q.append((ni,nj))
        # 인구 이동이 더 이상 발생하지 않는다면
        if unionNum == N*N: return days;
        days += 1;

        # 2. 국경선이 열려있어 인접 칸만을 이용해 이동할 수 있으면, 그 나라 전체는 하루동안 연합
        # 3. 연합을 이루는 각 칸 인구수는 (연합 인구수) / (연합 칸개수) 가 된다. 소수점 버림

        # 1 : 1번 연합 인구 인동 후 인구 수, 2 : 2번 연합 인구 이동 후 인구 수 ...
        uPeople = {}
        for u in range(unionNum):
            uPeople[u+1] = unionPtoC[u][0] // unionPtoC[u][1];

        for i in range(N):
            for j in range(N):
                cMap[i][j] = uPeople[vMap[i][j]]

        # 4. 연합 해체 후 국경선 닫기

# Answer? 인구 이동이 며칠동안 발생하는가?
print(Solution())