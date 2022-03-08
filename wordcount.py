'''
name = input("Enter your name")
print(f"your name is {name}")
vowel_counter=0
vowels = ['a','e','i','o','u']
for letter in name:
    #if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    if letter in vowels:
        vowel_counter=vowel_counter+1
print(f"no of vowels in {name} = {vowel_counter}")
'''

line=input('Enter name')
count=0
for letter in line:
    count=count+1
print(count)