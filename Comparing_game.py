import random
flower = ['梅花','鑽石','紅心','黑桃']
poke = []
for i in range(1,14):
    for j in range(4):
        poke.append(flower[j]+str(i))

juge = int(input("請輸入1，代表抽一張牌"))
while juge !=1:
    print("請輸入1，強迫玩XD")
    juge = int(input("請輸入1，代表抽一張牌"))
player = random.choice(poke)
com = random.choice(poke)
if poke.index(player) == poke.index(com):
    print('Tight')
elif poke.index(player) > poke.index(com):
    print('***********\n* You win *\n***********')
else:
    print('You lose')
print('電腦的牌: %s\n玩家的牌: %s'%(com,player))
