import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
last_num = nums[-1]
arr = [ [0 for _ in range(21)] for _ in range(N-1)]
arr[0][nums[0]] = 1

for i in range(1,N-1):
    n2 = nums[i]
    for n1 in range(0,21):
        if arr[i-1][n1] != 0:
            if 0 <= n1 + n2 <= 20:
                arr[i][n1+n2] += arr[i-1][n1]
            if 0 <= n1 - n2 <= 20:
                arr[i][n1-n2] += arr[i-1][n1]

print(arr[-1][last_num] )