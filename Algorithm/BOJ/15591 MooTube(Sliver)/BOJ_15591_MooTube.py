import sys
from collections import deque
sys.stdin = open('input.txt')

# 입력
N, Q = map(int,input().split())
USADO = {}
for _ in range(N-1):
    p,q,r = map(int,input().split())
    if p not in USADO:
        USADO[p] = [(q,r)]
    else:
        USADO[p].append((q,r))
    if q not in USADO:
        USADO[q] = [(p,r)]
    else:
        USADO[q].append((p,r))

# BFS
def bfs(k: int, s: int):
    answer = 0
    visit = [0] * (N+1)
    visit[s] = 1
    q = deque([(s,10**10 + 1)])

    while q:
        v,pr = q.popleft()
        for wr in USADO[v]:
            w,r = wr
            r = min(pr,r)
            if k <= r and visit[w] == 0:
                answer += 1
                visit[w] = 1
                q.append((w,r))

    return answer

# 결과
for _ in range(Q):
    k,v = map(int,input().split())
    print(bfs(k,v))
