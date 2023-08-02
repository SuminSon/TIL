import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 기차 1개 당 20개의 일렬 좌석.
# 1 i x : i번째 기차 x번째 좌석에 사람 채우기. 이미 타있다면 아무 행동 X
# 2 i x : i번째 기차 x번째 좌석에 앉은 사람이 하차. 빈 자리면 아무 행동 X
# 3 i : i번째 기차에 앉은 승객들이 모두 한 칸씩 뒤로 간다. k번째 사람이 k+1 번째
# 20번째 자리에 사람이 타고 있다면 그 사람은 명령 후 하차
# 4 i : i번째 기차에 앉은 승객들이 모두 한 칸씩 앞으로 간다. k번째 사람이 k-1 번째
# 1번째 자리에 사람이 타고 있다면 그 사람은 명령 후 하차

T, Cmd = map(int,input().split())
trains = [0]*T
memo = []

# print(trains)
for _ in range(Cmd):
    cmdline = list(map(int,input().split()))
    # 승객 개인 승하차
    if cmdline[0] == 1:
        t, s = cmdline[1], cmdline[2]
        trains[t-1] |= (1<<(s-1))
    elif cmdline[0] == 2:
        t, s = cmdline[1], cmdline[2]
        trains[t-1] &= ~(1<<(s-1))
    # 일렬 이동
    elif cmdline[0] == 3:
        t = cmdline[1]
        trains[t-1] = trains[t-1] << 1
        # 20을 넘어가면 제거해줘야지용
        if trains[t-1] >= 2*20:
            trains[t-1] &= ~(1<<(20))
    elif cmdline[0] == 4:
        t = cmdline[1]
        trains[t-1] = trains[t-1] >> 1

answer = 0
for t in range(T):
    if trains[t] not in memo:
        answer += 1
        memo.append(trains[t])
print(answer)