# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def findDivisor(number=0,maxDiv=0):
    if number is None  or maxDiv is None:
        print('No number defined!')
    maxDiv = range(2,maxDiv+1)
    divisor = []
    for elements in maxDiv:
        if number % elements == 0:
            divisor.append(elements)
    for index,display in enumerate(divisor, start=1):
        print('{}.) Divisor of -> {} Divided up to {} time(s)!'.format(index,display,number//display))

while True:
    try:
        number = int(input("Enter a Number: "))
        maxDiv = int(input('Enter the maximum range to divide: '))
    except ValueError:
        print('Only numbers are allowed!\nTry again!')
        continue
    else:
        findDivisor(number,maxDiv)
        break

