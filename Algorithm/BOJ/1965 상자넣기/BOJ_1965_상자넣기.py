import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
max_b = [ 1 for _ in range(n) ]
for b in range(1, n):
    max_box = 0
    for bb in range(b-1,-1,-1):
        if box[bb] < box[b]:
            if max_box < max_b[bb]:
                max_box = max_b[bb]
    max_b[b] += max_box



#print(box)
#print(max_b)
print(max(max_b))