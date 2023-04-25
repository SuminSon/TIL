import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    nodes[v] = 1
    for w in tree[v]:
        if nodes[w] == 0:
            dfs(w)
            nodes[v] += nodes[w]

N, R, Q = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    U,V = map(int,input().split())
    tree[U].append(V)
    tree[V].append(U)

nodes = [0 for _ in range(N+1)]
dfs(R)
for _ in range(Q):
    print(nodes[int(input())])

