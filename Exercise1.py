#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import datetime

def printAgeName(name,age):
    yrsOld = (100 - age) +datetime.datetime.now().year
    print('''Hello {Name}!
Your Current age is {age}!
You will be 100 in the year {yrsOld}!\n'''.format(Name=name,age=age,yrsOld=yrsOld))

while True:
    name = input("Enter your name: ")
    if not name.isalpha():
        print('Only letters are allowed! \n Try Again!')
        continue
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print('''This is not a number!
Try Again!\n''')
        continue
    else:
        break
printAgeName(name,age)
while True:
    try:
        copies = int(input('''How many copies would you like to print?
Enter 0 to Escape: '''))
        print('\n')
    except ValueError:
        print('''This is not a number!
Try Again!\n''')
        continue
    else:
        break
if copies != 0:
    for repeat in range(copies):
        printAgeName(name,age)