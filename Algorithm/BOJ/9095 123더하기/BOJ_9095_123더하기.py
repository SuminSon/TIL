import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    d = deque([1, 2, 4])
    n = int(input())
    if n>3:
        for _ in range(n-3):
            d.append(d[2]+d[1]+d[0])
            d.popleft()
        print(d[2])
    else:
        print(d[n-1])

