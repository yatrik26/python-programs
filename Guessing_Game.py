# The Gusseing Game
import random

n=20
gussed=int(n*random.random())+1
guess=0

while guess!=gussed:
     guess=int(input('New number = '))
     if guess>0:
         if guess>gussed:
            print('too large')
         elif guess<gussed:
            print('too small')
     else:
        print('sorry')
        break
else:
    print('congo')