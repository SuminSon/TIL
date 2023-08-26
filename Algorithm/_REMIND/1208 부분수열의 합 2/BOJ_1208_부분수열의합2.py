import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,S = map(int,input().split())
sequence = list(map(int,input().split()))

mid = N // 2
e = N
leftSums = {}
rightSums = {}

answer = 0
def leftSeq(st:int, sum:int, isSet = False):
    global answer
    if(st == mid):
        if isSet:
            if sum not in leftSums:
                leftSums[sum] = 1
            else:
                leftSums[sum] += 1
        return
    leftSeq(st+1, sum+sequence[st], True);
    leftSeq(st+1, sum, isSet);

def rightSeq(st:int, sum:int, isSet = False):
    global answer
    if(st == e):
        if isSet:
            if sum not in rightSums:
                rightSums[sum] = 1
            else:
                rightSums[sum] += 1
        return
    rightSeq(st+1, sum+sequence[st], True);
    rightSeq(st+1, sum, isSet);

leftSeq(0,0)
rightSeq(mid,0)

if S in leftSums:
    answer += leftSums[S]
if S in rightSums:
    answer += rightSums[S]

for l in leftSums:
    if S-l in rightSums:
        answer += (leftSums[l] * rightSums[S-l])

print(answer)