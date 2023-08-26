import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline



N,M = map(int,input().split())

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        a,b = y,x
    else:
        a,b = x,y

    if rank[x] == rank[y]:
        rank[b] += 1

    parent[a] = b

edges = []
result = []

for _ in range(M):
    A,B,C = map(int,input().split())
    edges.append((C,A,B))

edges.sort()

# 크루스칼
# 낮은 코스트의 간선부터 연결.
# 
for edge in edges:
    cost, a, b = edge

    if find(a) != find(b):
        union(a,b)
        result.append(cost)

print(sum(result[:-1]))