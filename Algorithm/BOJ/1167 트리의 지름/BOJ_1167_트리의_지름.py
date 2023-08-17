import sys

tree = {}
V = int(input())
for _ in range(V):
    nodes = list(map(int,input().split()))
    P = nodes[0]
    tree[P] = []
    for i in range(1,len(nodes)-2,2):
        tree[P].append((nodes[i],nodes[i+1]))

answer = 0
B = 0
stack = [(1,0)]
visit = [0] * (V+1)
while stack:
    v,cost = stack.pop()
    visit[v] = 1
    for wc in tree[v]:
        w,c = wc
        if visit[w] == 0:
            if answer < c + cost:
                answer = c + cost
                B = w
            stack.append((w, c + cost))

stack = [(B,0)]
visit = [0] * (V+1)
while stack:
    v,cost = stack.pop()
    visit[v] = 1
    for wc in tree[v]:
        w,c = wc
        if visit[w] == 0:
            if answer < c + cost:
                answer = c + cost
            stack.append((w, c + cost))

print(answer)