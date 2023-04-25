import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

N, M = map(int,input().split())
paths = defaultdict(list)
for m in range(M):
    p1, p2 = map(int,input().split())
    paths[p1].append(p2)
    paths[p2].append(p1)

kbnum = [0 for _ in range(N+1)]
for s in range(1,N+1):
    visited = [10**8 for _ in range(N + 1)]
    q = deque([(s)])
    visited[s] = 0
    while q:
        v = q.popleft()
        for w in paths[v]:
            if visited[w] > visited[v] + 1 and w != s:
                visited[w] = visited[v] + 1
                q.append(w)

    kbnum[s] = sum(visited[1:])

for kbp in range(1,N+1):
    if kbnum[kbp] == min(kbnum[1:]):
        print(kbp)
        break