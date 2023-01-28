import random
import os
from words import *
os.system('cls')
print('Welcome to Word Guessing Game')
print('-----------------------------')
p_name=input('Enter Your Name : ')
while True:
    print('>>Levels')
    print('1. Easy  |2. Medium  |3. Hard')
    print('Hi,',p_name,end=' ')
    ch=int(input('Choose level : '))
    while(ch<1 or ch>3):
        ch=int(input('Invalid!..Try again : '))
    if(ch==1):
        print('<<< Easy Level >>>')
        s=l_e[random.randrange(len(l_e)-1)]
        s1=list(s)
        random.shuffle(s1)
        while(s1==list(s)):
            random.shuffle(s1)
    elif(ch==2):
        print('<<< Medium Level >>>')
        s=l_m[random.randrange(len(l_m)-1)]
        s1=list(s)
        random.shuffle(s1)
        while(s1==list(s)):
            random.shuffle(s1)
    elif(ch==3):
        print('<<< Hard Level >>>')
        s=l_h[random.randrange(len(l_h)-1)]
        s1=list(s)
        random.shuffle(s1)
        while(s1==list(s)):
            random.shuffle(s1)
       
    for x in s1:
        print(x,end='')
    print()
    word=input('Guess the word : ')
    if(s==word):
        print('Congratulations!!! You win')
    else:
        print('Opps!!! Better luck next time')
    #Want to play again
    x=input('Do you want to play it again ? y/n : ')
    while(x!='y' and x!='n'):
        print('Invalid ! ...Try again')
        x=input()
    os.system('cls')
    if(x=='n'):
        break   
    print('Hey',p_name,',Welcome back!')
    print('-----------------------------')