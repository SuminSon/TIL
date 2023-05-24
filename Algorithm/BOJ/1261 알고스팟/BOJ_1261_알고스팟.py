import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 가로 N 세로 M
N,M = map(int,input().split())
arr = [list(map(int, input().rstrip())) for _ in range(M)]
visit = [[10**8]*N for _ in range(M)]
# 문제상의 (N,M) ... 즉 (N-1, M-1)에 도달할 때 최소 칸부심 횟수
q = deque([(0,0)])
visit[0][0] = 0
dn,dm = [1,-1,0,0],[0,0,1,-1]
while q:
    vm,vn = q.popleft()

    if vn == N-1 and vm == M-1:
        print(visit[vm][vn])
        break

    for k in range(4):
        vnn, vmm = vn + dn[k], vm + dm[k]
        if 0<=vnn<N and 0<=vmm<M:
            if visit[vmm][vnn] >  arr[vmm][vnn] + visit[vm][vn]:
                visit[vmm][vnn] = arr[vmm][vnn] + visit[vm][vn]
                if arr[vmm][vnn] == 0: q.appendleft((vmm,vnn))
                else: q.append((vmm,vnn))

