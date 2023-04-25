import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int,input().split()))
conv1 = deque(arr[0:N])
conv2 = deque(arr[N:2*N])
# conv1에 로봇이 올라간 여부를 0/1 로 나타냄
conv_r = deque([0 for _ in range(N)])

broken_block = 0
level = 0

while broken_block < K:
    level += 1

    # 컨베이어 벨트 이동
    conv2.appendleft(conv1.pop())
    conv1.appendleft(conv2.pop())
    conv_r.appendleft(0)
    conv_r.pop()

    # 내려
    if conv_r[-1] == 1:
        conv_r[-1] = 0

    # 로봇 자가이동
    for r in range(len(conv_r)-2,0,-1):
        if conv_r[r] == 1 and conv_r[r+1] == 0 and conv1[r+1] >= 1:
            conv_r[r] = 0
            conv_r[r+1] = 1
            conv1[r+1] -= 1
            if conv1[r+1] == 0: broken_block += 1

    # 내려
    if conv_r[-1] == 1:
        conv_r[-1] = 0

    if conv1[0] > 0  and conv_r[0] == 0:
        conv_r[0] = 1
        conv1[0] -= 1
        if conv1[0] == 0: broken_block += 1

print(level)