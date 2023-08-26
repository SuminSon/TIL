import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
print(board)

# 1 놓을 수 있는 곳
# 0 놓을 수 없는 곳


# [참고 아이디어]
# 체스판의 교차칸(흰/검)에 대해, 흰색 자리와 검은색 자리에 있는 비숍은 절대 서로 만나지 않는다.
# 즉, (i+j)%2 가 홀수인 경우와 짝수인 경우를 별개의 경우로 인식해 각각의 비숍 최대값을 구한 후 더한다.
# 이를 통해 탐색범위를 2^100에서 2^25 정도까지 줄일 수 있다.
# 놓을 수 있는 칸에 대해 기록하는 방법....
# 대각선 탈락시키기?

for i in range(N):
    for j in range(N):
        if (i + j)%2:
            # 우상향
            # 10 30 41 43
            # 좌하향
            # 14 34 43 31
            print("0 ",end='')
        else:
            # 우상향
            # 00 20 40 42 44
            # 좌하향
            # 04 24 44 42 40
            print("1 ", end='')
    print()