import sys
sys.stdin = open('input.txt')

def dfs(erase):
    removed.append(erase)
    if erase not in tree:
        return
    for c in tree[erase]:
        dfs(c)

N = int(input())
parent = list(map(int,input().split()))
erase = int(input())
tree={}

for n in range(N):
    if parent[n] not in tree:
        tree[parent[n]]=[n]
    else:
        tree[parent[n]].append(n)

removed=[]
#print(parent)
dfs(erase)
#print(tree)
#print(removed)

for r in removed:
    if r in tree:
        del tree[r]
    if parent[r] in tree:
        tree[parent[r]].remove(r)

#print(tree)
cnt = 0
for t in tree:

    if tree[t] == [] and t != -1:
        cnt+=1

    for c in tree[t]:
        if c not in tree:
            cnt+=1

print(cnt)




