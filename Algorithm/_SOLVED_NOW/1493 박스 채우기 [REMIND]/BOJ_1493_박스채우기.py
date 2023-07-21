import sys
sys.stdin = open('input.txt')

# l 길이 w 너비 h 높이
l,w,h = map(int,input().split())
N = (int)(input())
AB = [0] * 21
mA = 0
for n in range(N):
    A,B = map(int,input().split())
    AB[A] = B
    mA = A

# answer 정답
# nowBox 현재 채워진 부분의 부피. 박스 종류 부피 * 개수로 표현되기 위해 박스가 작아질수록 8씩 곱해진다
# 이를 통해 해당 종류 박스가 전체를 채우는 개수 - 채워진 부분을 채우는 개수 = 채우는데 필요한 개수를 구한다
# nowBox가 채워야하는 부분을 전부 채우면 값을 출력하고,
# 모든 처리가 끝난 후에도 박스가 채워지지 못했다면 -1 출력

answer = nowBox = 0
for a in range(A,-1,-1):
    nowBox *= 8
    b = 2**a
    beSetBox = (l//b) * (w//b) * (h//b)  - nowBox
    beSetBox = min(AB[a] ,beSetBox)

    answer += beSetBox
    nowBox += beSetBox

if nowBox == l*w*h:
    print(answer)
else:
    print(-1)