import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global num
    visited[v]=1
    node=[v,num,num]
    for w in graph[v]:
        if visited[w]==0:
            num+=1
            dfs(w)
    num += 1
    node[2] = num
    nodes[v] = node

N=int(input())
graph=[None for _ in range(N+1)]
for _ in range(N):
    v,*arr=map(int,input().split())
    graph[v]=sorted(arr[:-1])
#print(graph)
S=int(input())
visited=[0 for _ in range(N+1)]
num=1
nodes=[None for _ in range(N+1)]
dfs(S)
for n in nodes[1:]:
    print(n[0],n[1],n[2])