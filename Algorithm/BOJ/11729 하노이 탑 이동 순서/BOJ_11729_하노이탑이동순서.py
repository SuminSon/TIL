import sys
sys.stdin = open('input.txt')
input=sys.stdin.readline

def dfs(K,s,v,g):
    global cnt
    if K==1:
        result.append([s,g])
        cnt+=1
    else:
        dfs(K-1,s,g,v)
        dfs(1,s,v,g)
        dfs(K-1,v,s,g)

K=int(input())
cnt=0
result=[]
dfs(K,1,2,3)
print(cnt)
for r in result:
    print(r[0],r[1])