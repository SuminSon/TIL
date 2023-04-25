import sys
sys.stdin = open('input.txt')

K, N = map(int,input().split())
lans = [int(input()) for _ in range(K)]
lans.sort(reverse=True)
result = sum(lans) // N
isN = 0
while isN != N :
    isN = 0
    for lan in lans:
        isN += lan // result
    if isN < N:
        result = lans[0] // ((lans[0] // result)+1)
print(result)