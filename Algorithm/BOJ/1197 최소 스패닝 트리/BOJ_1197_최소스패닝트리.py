import sys
import heapq
import collections
sys.stdin = open('input.txt')

V,E = map(int,input().split())
graph = collections.defaultdict(list) # 빈 그래프 생성
visit = [0] * (V+1)

for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A].append((C,A,B))
    graph[B].append((C,B,A))

# 프림 알고리즘
def prim(graph, start):
    visit[start] = 1
    near = graph[start]
    heapq.heapify(near)
    mst = []
    total_weight = 0

    while near:
        w, u, v = heapq.heappop(near) # 가중치 적은 간선부터 빼내기~!

        if visit[v] == 0:
            visit[v] = 1
            mst.append((u,v))
            total_weight += w

            # 다음 간선 탐색.. 방문한 노드 아닐 때 넣기
            for edge in graph[v]:
                if visit[edge[2]] == 0:
                    heapq.heappush(near, edge)
    return total_weight

print(prim(graph,1))