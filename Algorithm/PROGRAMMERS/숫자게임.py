def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    bdx = 0
    for i in range(len(A)):
        a = A[i]
        for j in range(bdx,len(B)):
            b = B[j]
            if a < b:
                answer += 1
                bdx = j+1
                break
        i += 1
    return answer

solution([2,2,2,2],[1,1,1,1])