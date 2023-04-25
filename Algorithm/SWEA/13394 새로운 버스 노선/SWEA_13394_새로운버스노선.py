import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    # 0번 인덱스에 타입, 이후 출발지부터 도착지까지 정차하는 정류장들로 리스트
    bus_sch=[]
    for _ in range(N):
        t,a,b=map(int,input().split())
        if t==1:
            bus=[t,a]+(list(range(a+1,b)))
        elif t==2:
            bus = [t,a] + (list(range(a+2, b,2)))
        elif t==3:
            bus=[t,a]
            for i in range(a+1,b):
                if (a%2==0 and i%4==0) or (a%2!=0 and i%3==0 and i%10!=0):
                    bus +=[i]
        bus+=[b]
        bus_sch.append(bus)
    # 각 버스 정류장 번호를 key, 정차한 버스 수를 val로 하는 딕셔너리
    visited={}
    for bus in bus_sch:
        for i in range(1,len(bus)):
            if bus[i] not in visited:
                visited[bus[i]]=1
            else:
                visited[bus[i]]+=1

    # value 최댓값 찾아서 출력
    result=0
    for r in visited.values():
        if result<r:
            result=r
    print(f'#{tc} {result}')