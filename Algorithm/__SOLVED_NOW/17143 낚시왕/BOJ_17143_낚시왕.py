import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R,C,M = map(int,input().split())
fspot = [[(0,0,0)]*C for _ in range(R)]
# print(fspot)
for _ in range(M):
    # (r,c) 위치
    # s 속력, d 이동방향, z 크기
    r,c,s,d,z = map(int,input().split())
    fspot[r-1][c-1] = (s,d,z)

for r in range(R):
    print(fspot[r])

# 낚시왕이 한칸 움직이고 상어픽업
def pickupShark(turn:int):
    pass

# 1초동안 상어들이 움직임
# 같은 칸에 접하게 된 상어들은 별도기록
def moveShark():
    pass

# 같은 칸에 접한 상어들 중 가장 큰 놈만 냅두고 다 사라짐
def eatShark():
    pass

