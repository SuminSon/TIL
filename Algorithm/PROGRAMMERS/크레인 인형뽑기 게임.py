# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3#
# 프로그래머스는 함수 내부에 구현해 값을 return하는 형태로 문제를 풉니다.
# 제출 시 모든 테스트케이스를 점검하고, 가장 점수 높은 것으로 반영된다고 하네요

def solution(board, moves):
    answer = 0
    stack=[]
    # 크레인에서 moves만큼 인형을 집습니다.
    # moves가 1번부터 주어지므로 인덱스로 받기 위해 -1 해줘야
    # 행과 열 위치에 주의
    for m in moves:
        crain=0
        for h in range(len(board)):
            if board[h][m-1]!=0:
                crain,board[h][m-1]=board[h][m-1],0
                break
        # 크레인이 무언가를 집었다면
        if crain!=0:
            # 스택이 차있고, 최근 인형과 크레인 인형이 같으면 2개 지움
            if stack and stack[-1]==crain:
                stack.pop()
                answer+=2
            # 지울 조건 아니면 스택에 집어넣음
            else:
                stack.append(crain)
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
# 답 = 4개
print(solution(board, moves))