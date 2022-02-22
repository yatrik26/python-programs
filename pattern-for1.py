'''
1 2 1 2 1         
1 2 1 1
1 2 1
1 2
1
'''

for row in range(1,6):
    for column in range(1,row+1):
        if column%2==0:
            print('2',end=' ')
        else:
            print('1',end=' ')
    print('')
    