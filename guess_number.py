import random
llimit, rlimit = 1, 99
number = random.randint(llimit, rlimit)
guess = -1
while guess != number:
    guess = int(input('請猜%i至%i間其中1個整數，不包含%i及%i'%(llimit, rlimit, llimit, rlimit)))
    while guess <= llimit or guess >= rlimit:
        guess = int(input('不要鬧了，請猜%i至%i間其中1個整數，不包含%i及%i'%(llimit, rlimit, llimit, rlimit)))
        if guess > number:
        llimit = llimit
        rlimit = guess
    elif guess < number:
        llimit = guess
        rlimit = rlimit
print('遊戲結束，因為終極密碼為%i'%number)
