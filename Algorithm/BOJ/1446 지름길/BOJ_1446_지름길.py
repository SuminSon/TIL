import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, D = map(int,input().split())
path = []
check = [0,D]
min_go = {0:0, D:D}
for _ in range(N):
    s, g, l = map(int,input().split())
    if g <= D and g - s > l:
        path.append((s,g,l))
        check.append(s)
        check.append(g)
        min_go[s] = s

path.sort(key=lambda x:x[0])
check = list(set(check))
check.sort()

for p in path:
    s, g, l = p
    min_go[g] = min(g, l + min_go[s], min_go[g]) if g in min_go else min(g, l + min_go[s])
    for pp in min_go:
        if pp > g: min_go[pp] = min(min_go[pp], min_go[g] + pp - g)
print(min_go[D])