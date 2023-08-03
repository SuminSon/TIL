import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = 0
N, K = map(int,input().split())
wTable = []
allBit = set()
B = 0
for _ in range(N):
    word = input().rstrip()
    wBit = 0
    for w in word:
        wNum = ord(w) - 97
        wBit |= (1<<wNum)
        allBit.add(wNum)
    wTable.append(wBit)

# 각 경우의 수 비트일 때 배울 수 있는 단어 개수의 최댓값을 구한다
def getAnswer(bct):
    global answer
    myBit = 0
    thisAns = 0
    for b in bct:
        myBit |= (1<<b)
    for w in wTable:
        if myBit & w == w:
            thisAns += 1
    answer = max(answer,thisAns)

# B개에서 K개 bit를 고르는 경우의 수
B = len(allBit)
allBit = list(allBit)
visit = [0]*26
visit[0] = visit[2] = visit[8] = visit[13] = visit[19] = 1
def bCk(K, nb = 0, elem=[0,2,8,13,19]):
    if K < 5:
        return
    if K-5 == 0:
        getAnswer(elem)
        return
    for b in range(nb,len(allBit)):
        if visit[allBit[b]] == 0:
            visit[allBit[b]] = 1
            bCk(K-1, b, elem + [allBit[b]])
            visit[allBit[b]] = 0

bCk(K if B>=K else B)
print(answer)