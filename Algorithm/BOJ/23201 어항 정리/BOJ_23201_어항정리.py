# https://www.acmicpc.net/problem/23291

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int,input().split())
space = [[-1] * N for _ in range(N)]
spaceAddMin = [[0] * N for _ in range(N)]
space[N - 1] = list(map(int,input().split()))
count = 0

def minPutFish():
    minVal = min(space[N - 1])
    for i in range(N):
        if space[N - 1][i] == minVal:
            space[N - 1][i] += 1

def fold1():
    cx = N-1
    cy = 0
    hx = 0
    for j in range(N):
        height = 0
        # 첫 시작점과 그 때의 높이를 측정
        for i in range(N - 1, -1, -1):
            # print(f'space[{i}][{j}] = {space[i][j]}')
            if space[i][j] == -1 :
                hx = i+1
                break
            else: height += 1
        # 높이 측정 후 가로로 같은 높이가 얼마나 더 있는지 확인
        # 뒤집기 당하는 중심 좌표를 찾는다
        # print(f'h = {height} hx ={hx }')
        if height > 1:
            for k in range(1,N-j):
                # print(f'h={height} space[{hx }][{j+k}] = {space[hx][j+k]}')
                if space[hx][j + k] == -1:
                    cy = j + k - 1
                    # print(cy, height)
                    break
                # -1 영역이 더이상 없다(접을 수 없다)
                if j+k == N-1: return 0;
            # 더 이상 못 접는다. 길이보다 얹을 곳이 짧아서
            # print(height, N-1-cy)
            if height > N-1-cy:
                return 0;
            break

        elif height == 1:
            cy = j
            break;

    for mi in range(N-1):
        for mj in range(cy + 1):
            if space[cx-mi][cy-mj] == -1:
                break
            else:
                space[cx-mi][cy-mj], space[cx-1-mj][cy+mi+1] = space[cx-1-mj][cy+mi+1], space[cx-mi][cy-mj]
    return 1;

dx,dy = [1,-1,0,0], [0,0,-1,1]
def divideFish():
    spaceAddMin = [[0] * N for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            for k in range(4):
                si, sj = i + dx[k], j + dy[k]
                if(si>=N or sj>=N or si==-1 or sj == -1): continue;
                if space[i][j] == -1 or space[si][sj] == -1: continue;
                if(space[i][j] > space[si][sj] and (space[i][j] - space[si][sj])//5 > 0):
                    d = (space[i][j] - space[si][sj])// 5
                    spaceAddMin[i][j] -= d
                    spaceAddMin[si][sj] += d
                    #
                    # print(f'space [{i}][{j}] = {space[i][j]}')
                    # print(f'space [{si}][{sj}] = {space[si][sj]}')
                    # print(f'd={d}\n')
                    
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            space[i][j] += spaceAddMin[i][j]

# 한 줄로 재배치
def oneLineSet():
    setNum = 0
    for j in range(N):
        if space[N-1][j] != -1:
            for i in range(N):
                if space[N-1-i][j] != -1:
                    space[N-1][setNum], space[N-1-i][j] = space[N-1-i][j], space[N-1][setNum]
                    setNum+=1


def twoFold():
    for mi in range(N-1):
        for mj in range(N//2 + 1):
            if space[N-1-mi][N//2-1 -mj] == -1 or (N-1-mi<0) or (N//2-1 -mj<0):
                break
            else:
                space[N-1-mi][N//2-1 -mj], space[N-1-1][N//2 +mj] = space[N-1-1][N//2 +mj], space[N-1-mi][N//2-1 -mj]

def threeFold():
    for mi in range(2):
        for mj in range(N-1-(N//4) + 1):
            if space[N-2+mi][N-1-(N//4)-mj] == -1:
                break
            else:
                space[N-2+mi][N-1-(N//4)-mj], space[N-3-mi][N-(N//4)+mj] = space[N-3-mi][N-(N//4)+mj], space[N-2+mi][N-1-(N//4)-mj]


def oneChange():
    # 초기 어항
    minPutFish()

    # 될 때까지 접기
    v = fold1()
    while v==1:
        v = fold1()

    # 물고기 나누기
    divideFish()

    # 한 줄로 재배치
    oneLineSet()

    twoFold()

    threeFold()

    divideFish()

    # 한 줄로 재배치
    oneLineSet()

    return 1

result = 0
while max(space[N-1]) - min(space[N-1]) > K:
    result += oneChange()
print(result)
