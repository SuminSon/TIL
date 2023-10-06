import sys
import heapq
sys.stdin = open('input.txt')

N = (int)(input())
cards = [(int)(input()) for _ in range(N)]
heapq.heapify(cards)

answer = 0
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    nc = c1 + c2
    answer += nc
    heapq.heappush(cards,nc)

print(answer)