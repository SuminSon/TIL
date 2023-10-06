import sys
import heapq
sys.stdin = open('input.txt')

N = (int)(input())
k = (int)(input())

s, e = 0, k
while s <= e:
    mid = (s+e) // 2
    cnt = 0

    # k보다 작은 수의 곱이 몇 개인지 세면 k는 그 값 + 1 이 됩니다.
    # 이 때 mid는 몇번째가 아닌, 중앙의 숫자를 의미합니다.
    # mid보다 작은 수의 곱이 몇개인지 센다면 mid가 몇 번째 수인지 알 수 있습니다.
    #

    # mid번째 값보다 작은 값으 개수를 cnt로 셉니다.
    # 이 때,
    for i in range(1,n+1):
        cnt += min(mid//i, N)