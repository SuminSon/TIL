#python hello.py

player=5
greeting='반갑습니다.'

def bot(player):
    while player>0:
        print(greeting)
        player=player-1

#20명 모두에게 인사를 하려면?
'''
for i in range(0,player):
    print(greeting)

print()
while player>0:
    print(greeting)
    player=player-1
'''