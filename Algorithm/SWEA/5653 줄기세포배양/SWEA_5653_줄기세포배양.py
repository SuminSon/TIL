import sys
sys.stdin = open('input.txt')

di, dj = [1,-1,0,0],[0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # sepo = (i좌표, j좌표, 생명력, 태어난 시간, 비활성 1 / 활성 2 / 죽음 0)
    time = 0
    sepos = []
    arrs = {}
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                sepos.append((i,j,arr[i][j],time, 1))
                arrs[(i,j)] = sepos[-1]

    while time < K:
        time += 1
        #print(f'time : {time}')
        for sdx in range(len(sepos)):
            i, j, k, stime, stype = sepos[sdx]
            if stype == 1 and time - stime == k:
                sepos[sdx] = (i,j,k,stime,2)
            if stype == 2: # 활성상태 -> 번식
                if time - stime == 2*k: # 때가 되면 죽음
                    sepos[sdx] = (i, j, k, stime, 0)
                for d in range(4): 
                    dii, djj = i+di[d], j+dj[d]
                    if (dii,djj) not in arrs: # 그 자리가 비어있다면 새 세포를 추가
                        sepos.append((dii,djj,k,time,1))
                        arrs[(dii,djj)] = (dii,djj,k,time,1)
                    elif arrs[(dii,djj)][3] == time: # 나랑 같은 시점에 생겼다 == 동시에 번식
                        if arrs[(dii,djj)][2] < k:
                            sepos[sepos.index((dii, djj, k, stime, 1))] = (dii,djj,k,time,1)
                            arrs[(dii, djj)] = (dii,djj,k,time,1)
    '''        
            for s in sepos:
                print(f'i:{s[0]} j:{s[1]} k:{s[2]} 생성된 시간:{s[3]}, 현재상태{s[4]}')
        print('-'*30)
    '''
    result = 0
    for sepo in sepos:
        if sepo[4] != 0: result += 1

    print(f'#{tc} {result}')