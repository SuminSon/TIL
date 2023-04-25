import sys
import heapq
from collections import  defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dijkstra(start:int, goal:int):
    visited = [10 ** 9 for _ in range(N + 1)]
    q = []
    heapq.heappush(q,(0,start))
    visited[start] = 0
    while q:
        cost, v = heapq.heappop(q)
        for c, w in path[v]:
            if visited[w] > visited[v] + c:
                visited[w] = visited[v] + c
                heapq.heappush(q,(c, w))
    return visited[goal]

N, E = map(int,input().split())
path = defaultdict(list)
for e in range(E):
    a, b, c = map(int,input().split())
    path[a].append((c,b))
    path[b].append((c,a))
a, b = map(int,input().split())

sabN = dijkstra(1,a) + dijkstra(a,b) + dijkstra(b,N)
sbaN = dijkstra(1,b) + dijkstra(b,a) + dijkstra(a,N)
result = min(sabN,sbaN)
print('-1' if result >= 10 ** 9 else result)