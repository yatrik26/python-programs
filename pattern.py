#write a program to print following pattern using for loops
# 1,4,9,16,25.....,100
'''
for number in range(1,11):
    square=number**2
    print(square,end=' ')
'''
#1,3,5,7,9....100

for number in range(1,100,2): #2=step
    print(number,end=' ')