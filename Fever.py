# write a program to detect fever level and define different stages of it.

print("Enter patient's fever details")
print('''
        1-F
        2-C''')

choice=int(input())
if choice==1:
        print("Enter your body tempreature in farenhit")
        F=float(input('TEMPREATURE= '))
        if F>=41.1 and F<=42:
                print('Hyperpyrexia')
        elif F>=40.5 and F<41.1:
                print('very high fever')
        elif F>=39.4 and F<40.5:
                print('high fever')
        elif F>=37.5 and F<39.4:
                print('fever ')
        else:
                print('Check Again')
elif choice==2:
        print("Enter your body tempreature in celcius")
        C=float(input('TEMPREATURE= '))
        if C>=106 and C<=107:
                print('Hyperpyrexia')
        elif C>=105 and C<106:
                print('very high fever')
        elif C>=103 and C<105:
                print('high fever')
        elif C>=98.6 and C<103:
                print('fever ')
        else:
                print('Check Again')
else:
        print('wrong choice')
