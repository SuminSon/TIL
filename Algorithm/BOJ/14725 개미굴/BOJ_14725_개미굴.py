import sys
sys.stdin = open('input.txt')

def dfs(t = 1, a = 0, path = []):
    if tree[t] == [] : return
    for words in tree[t] :
        if words[:-1] == path:
            print('--' * t, end='')
            print(words[-1])
            dfs(t+1,a,path+[words[-1]])

N = int(input())

tree = [[] for _ in range(16)]
for _ in range(N):
    wn , *words = input().split()

    for wi in range(len(words)):
        if words[:wi+1] not in tree[wi]:
            tree[wi].append(words[:wi+1])
for t in tree:
    t.sort(key=lambda x:(x[0],x[-1]))

print(tree)

for a in range(len(tree[0])):
    print(tree[0][a][0])
    dfs(1, a, tree[0][a])



