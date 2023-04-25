import sys
sys.stdin = open('input.txt')

N, d, k, c = map(int,input().split())
chobab = [int(input()) for _ in range(N)]
result = 0
for i in range(N):
    if (i+k) >= N: result = max(result, len(set(chobab[i:i + k] + chobab[:(i+k) % N] + [c])));
    else: result = max(result, len(set(chobab[i:i+k]+[c])));
print(result)