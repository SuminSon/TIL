import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int,input().split())
deck = list(map(int,input().split()))
chelsuPick = list(map(int,input().split()))

deck.sort()

print(deck)

# 이분 탐색으로 num보다 큰 수 중 덱에서 가장 작은 수를 찾는다
def winTo(num):



for c in chelsuPick:
    winTo(c)

