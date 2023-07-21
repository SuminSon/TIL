import sys
sys.stdin = open('input.txt')

Gp = [1]*10001
for i in range(2, 5001):
    if Gp[i]:
        k = 2
        while i*k<=10000:
            Gp[i*k] = 0
            k += 1

T = (int)(input())
for t in range(T):
    n = (int)(input())
    for i in range(n//2,1,-1):
        if Gp[i] and Gp[n-i]:
            print(f"{i} {n-i}")
            break

