import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
TP = list(map(int,input().split()))[1:]
partyList = [list(map(int,input().split()))[1:] for _ in range(M)]

# 진실을 아는 사람들은 노드 0을 루트로 갖도록 한다.

parent = [i for i in range(N+1)]
node_rank = [1 for i in range(N+1)]

for t in TP:
    parent[t] = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x != y:
        if x < y: parent[y] = x
        else: parent[x] = y

parties = []
for party in partyList:
    for i in range(len(party)-1):
        union(party[i], party[i+1])

answer = 0
for party in partyList:
    isTrueParty = False
    for i in range(len(party)):
        if find(party[i]) == 0:
            isTrueParty = True
            break
    if not isTrueParty:
        answer += 1

print(answer)