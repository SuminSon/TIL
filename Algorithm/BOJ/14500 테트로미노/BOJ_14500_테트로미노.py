import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,-1,1]
# 빠큐 제외 검사
def dfs(s:(int,int,int,int)):
    global tsums, visited

    x, y, k, sums = s

    if k == 4:
        if tsums < sums:
            tsums = sums
        return

    for d in range(4):
        dxx, dyy = x + dx[d], y + dy[d]
        if 0<=dxx<N and 0<=dyy<M and (dxx,dyy) not in visited:
            visited.append((dxx,dyy))
            dfs((dxx,dyy,k+1,sums+arr[dxx][dyy]))
            visited.pop()

# 빠큐 검사
# dx,dy 넷 중 세 방향에 대해 검사합니다.
# 0123 중 3개 선택하는 순열 만들어서 델타 탐색
def nPr(s:(int,int),idx=0, elem=[]):
    global tsums
    x,y = s
    for elem in [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]:
        sums = arr[x][y]
        for e in elem:
            dxx, dyy = x + dx[e], y + dy[e]
            if 0 <= dxx < N and 0 <= dyy < M:
                sums += arr[dxx][dyy]
            else:
                continue
        if tsums < sums:
            tsums = sums


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tsums = 0
for i in range(N):
    for j in range(M):
        visited = [(i,j)]
        dfs((i,j,1,arr[i][j]))
        nPr((i,j))

print(tsums)