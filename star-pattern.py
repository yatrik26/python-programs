'''
write a program to print following pattern
*
**
***
****
*****
'''
for row in range(1,6):
    for column in range(1,row+1):
        print('*',end=' ')
    print('')
    