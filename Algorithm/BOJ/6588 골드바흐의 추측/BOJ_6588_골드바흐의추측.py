import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

Ns = [1] * 1000001
Ns[0] = Ns[1] = 0
for i in range(3,1001,2):
    if Ns[i]:
        k = 2
        while i * k <= 1000000:
            Ns[i*k] = 0
            k += 1

N = -1
while True:
    N = (int)(input())
    if N == 0: break
    for i in range(3, 500001,2):
        isG = False
        if Ns[i] == 1 and Ns[N - i] == 1:
            print(f"{N} = {i} + {N-i}")
            isG = True
            break
    if not isG:
        print("Goldbach's conjecture is wrong.")

