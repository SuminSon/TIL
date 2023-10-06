import sys
from collections import deque
sys.stdin = open('input.txt')

# 3% 틀리다

N,K = map(int,input().split())
seq = list(map(int,input().split()))
index = {}
for i in range(K):
    if seq[i] in index:
        index[seq[i]].append(i)
    else:
        index[seq[i]] = [i]
print(seq)
print(index)

q = []
cur = 0
qInputNum = 0
for cur in range(K):
    if seq[cur] not in q:
        q.append(seq[cur])
        qInputNum += 1
    if qInputNum == N:
        break

answer = 0
while cur < K-1:
    cur += 1
    # 다음 순서가 이미 꼽혀있다면 넘어가기
    if seq[cur] in q:
        continue
    # 꼽혀있지 않다면 무얼 뽑을지 선택해야한다.
    else:
        print()
        print(f"first q {q}")
        # 현재 꼽힌 플러그 중, 추후에 재등장하는 플러그 개수
        cnt = 0
        offPlug = (0,0) # cur보다 큰 값이 있
        afterPlug = [0]*(max(seq)+1)
        for plug in q: # 꼽힌 플러그의
            for pdx in index[plug]: # 등록된 인덱스가
                if pdx > cur: # 현재 커서 이후에도 존재한다면?
                    cnt += 1
                    curdif = pdx - cur
                    afterPlug[plug] = 1
                    if offPlug[1] < curdif:
                        offPlug = (plug ,curdif)
                    break
        if cnt == 0: # 현재 플러그가 전부 재등장하지 않는다면 아무거나 뽑고 다음거 꼽기
            q.pop()
        elif 0 < cnt < len(q): # 등장하지 않는 나머지 중에 아무거나 뽑기 ㅋㅋ
            for qdx in range(len(q)-1,-1,-1):
                if afterPlug[q[qdx]] == 0:
                    q.remove(q[qdx])
                    break
        else: # 전부 재등장한다면 가장 나중에 등장하는거 뽑기
            q.remove(offPlug[0])
        q.append(seq[cur])
        answer += 1

        print(f"cur {cur} | cur_Value { seq[cur] } | q {q} | ")
        print()

print(answer)