import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 3101 토끼의 이동
# N 행렬의 크기
# K 토끼가 점프한 횟수
N, K = map(int,input().split())
jump_commend = list(input().rstrip())

dr = [[1,-1,0,0],[0,0,-1,1]]
D = {'D':0,'U':1,'L':2,'R':3}

nSumTable = [0]*N
nSumTable[0] = 1
s = 1
for s in range(1, N):
    nSumTable[s] = nSumTable[s-1] + s+1

answer = 1
pos = (0,0)
for jmp in jump_commend:
    i,j = pos
    ni,nj = i + dr[0][D[jmp]], j + dr[1][D[jmp]]
    nSum = ni + nj
    pos = (ni, nj)
    if nSum < N:
        S = nSumTable[nSum]
        if(nSum%2): answer += S - nj
        else: answer += S - ni
    else:
        ni, nj = N-ni-1, N-nj-1
        nSum = ni + nj
        S = nSumTable[nSum]
        if(nSum%2): answer += N**2 + 1 - (S - nj)
        else: answer += N**2 + 1 - (S - ni)
print(answer)
