import random
 
 
while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
     
    choice = int(input("1st User turn: "))
 
     
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
         
 

    if choice == 1:
        choice_name = 'Rock'
        print("1st user choice is: " + choice_name)
    elif choice == 2:
        choice_name = 'paper'
        print("1st user choice is: " + choice_name)
    else:
        choice_name = 'scissor'
        print("1st user choice is: " + choice_name)

    
    print("2nd user's turn" )
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    
    choice2=int(input('Enter choice of 2nd user: '))
    
    while choice2 > 3 or choice2 < 1:
        choice2=int(input('Enter valid choice'))

    if choice2 == 1:
        choice2_name='rock'
        print('2nd user choice is:' + choice2_name)
    elif choice2 == 2:
        choice2_name='paper'
        print('2nd user choice is:' + choice2_name)
    else:
        choice2_name='scissor'
        print('2nd user choice is:' + choice2_name)


    if ((choice==1 and choice2==1) or (choice==2 and choice2==2) or (choice==3 and choice2==3)):
       print("It's Draw")
    elif ((choice==1 and choice2==2) or (choice==1 and choice2==3) or (choice==3 and choice2==2)): 
        print("1st user wins")
    else:
        print("2nd user wins")    
    


         
    print('Do you want to play it again Y/N')
    ans=input()

    if ans == 'n' or ans == 'N':
        break

