import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# value error

# BOJ 1043 거짓말
# N : 사람 수 | M : 파티 수
# TP : 이야기의 진실을 아는 사람의 수, 번호 나열 (1~N번 사람)
# 각 파티마다 오는 사람의 수, 번호 나열 (1~N번 사람)
N, M = map(int,input().split())
TP = list(map(int,input().split()))[1:]
PP = [list(map(int,input().split()))[1:] for _ in range(M)]

# 거짓말을 들어선 안되는 이들을 비트로 저장
# 기존 인원 및 기존 인원과 함께 파티에 참석했던 사람도 함께 저장
tpBit = 0
q = deque([])
visit = [0]*(N+1)
for t in TP:
    visit[t] = 1
    tpBit |= (1 << t)
    q.append(t)
while q:
    tp = q.popleft()
    for party in PP:
        if tp in party:
            for person in party:
                if visit[person] == 0:
                    visit[person] = 1
                    tpBit |= (1 << person)
                    q.append(person)

answer = 0
for party in PP:
    pBit = 0
    for person in party:
        pBit |= (1 << (person))
        # 진실을 아는 사람이 없을 때 거짓말을 한다.
    if tpBit & pBit == 0:
        answer += 1

print(answer)
