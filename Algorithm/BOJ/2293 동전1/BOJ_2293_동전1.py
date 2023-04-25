import sys
sys.stdin = open('input.txt')

def ncr(k:int, coins:list, idx=0, elem=[]):
    global result
    if k == 0:
        result += 1
        print(elem)
        return
    for i in range(idx,len(coins)):
        if i == len(coins)-1 :
            if k % coins[i] != 0:
                return
            else:
                ncr(0, coins, i + 1, elem+[(coins[i], k// coins[i])])
                break
        for j in range(0,(k//coins[i])+1):
            ncr(k-coins[i]*j,coins,i+1,elem+[(coins[i],j)])


n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
result = 0
ncr(k,coins)
print(result)