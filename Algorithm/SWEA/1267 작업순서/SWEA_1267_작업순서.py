import sys
import pprint
sys.stdin=open('input.txt')

def dfs(v):
    global visited
    # 방문 내역 없으면 추가
    if v not in visited:
        visited.append(v)
    # 더이상 갈 길 없으면 그대로 돌아가기
    if v not in path:
        return
    # 모든 사전 작업이 끝난 것을 다음 작업으로 선택
    for w in path[v][1]:
        if all(x in visited for x in path[w][0]):
            dfs(w)

T=10
for tc in range(1,T+1):
    V,E=map(int,input().split())
    Ei=list(map(int,input().split()))
    path={}
    for p in range(0,len(Ei),2):
        if Ei[p] in path:
            path[Ei[p]][1].append(Ei[p + 1])
        else:
            path[Ei[p]]=[[],[Ei[p+1]]]
        if Ei[p+1] in path:
            path[Ei[p+1]][0].append(Ei[p])
        else:
            path[Ei[p+1]] = [[Ei[p]],[]]

    visited = []
    # 사전 작업 없는 시작점과
    # 아직 방문하지 않았으나 모든 사전 작업이 끝난 경우 이어서 새로 탐색
    for s in path:
         if (path[s][0]==[] or
            (any(x not in visited for x in path[s][1]) and
            (all(x in visited for x in path[s][0])))):
            if s not in visited:
                dfs(s)

    # 아예 노드 연결 없이 단독으로 존재하는 일 후속 처리
    for a in list(range(1,V+1)):
        if a not in visited:
            visited.append(a)

    result=' '.join(map(str,visited))
    print(f'#{tc} {result}')