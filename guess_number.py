import random   #載入隨機亂數套件
llimit, rlimit = 1, 99   #設定區間
number = random.randint(llimit, rlimit)     #讓電腦從區間內隨機挑選1個整數作為終極密碼
guess = -1    #為了讓while迴圈一定可以執行而給定的初始猜測值
while guess != number:   #迴圈，當猜測值不等於終極密碼時才執行
    guess = int(input('請猜%i至%i間其中1個整數，不包含%i及%i'%(llimit, rlimit, llimit, rlimit)))    #請輸入者輸入整數(開始猜測)
    while guess <= llimit or guess >= rlimit:   #為避免輸入者輸入不合理的整數而寫的迴圈
        guess = int(input('不要鬧了，請猜%i至%i間其中1個整數，不包含%i及%i'%(llimit, rlimit, llimit, rlimit)))
    if guess > number:      #調整區間
        llimit = llimit
        rlimit = guess
    elif guess < number:        #調整區間
        llimit = guess
        rlimit = rlimit
print('遊戲結束，因為終極密碼為%i'%number)
