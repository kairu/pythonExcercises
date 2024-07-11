# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#     If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
EVEN = 2
MULTIPLE_OF_FOUR = 4
def OddOrEven(number, Even=EVEN, asked = False):
    if asked:
        if number // Even and number % Even == 0:
            print('It divides Evenly!')
        else:
            print('It has a remainder of {}'.format(number%Even))
        quit()
    if number // MULTIPLE_OF_FOUR and number % MULTIPLE_OF_FOUR == 0:
        print('The number is a multiple of 4')
    elif number % Even == 0:
        print('The Number is Even')
    else:
        print('The Number is Odd')

def ErrorNumber(flag = 0):
    if flag == 0:
        print('Please input a number.\nTry Again!\n')
    elif flag == 1:
        print('Only letters are allowed!\n Try Again!')
    elif flag == 2:
        print('Please only input 1 character!')
    elif flag == 3:
        print('Only Input Y/y or N/n!')

while True:
    try:
        number = int(input('Input a number: '))
    except ValueError:
        ErrorNumber()
        continue
    else:
        OddOrEven(number)
        break

while True:
    ask = input('Input two numbers? Y/N: ')
    if not ask.isalpha():
        ErrorNumber(1)
        continue
    if len(ask) == 1:
        if ask.lower() == 'y':
            break
        elif ask.lower() == 'n':
            quit()
        else:
            ErrorNumber(3)
    else:
        ErrorNumber(2)
        continue

while True:
    try:
        number = int(input('Input number 1: '))
        number2 = int(input('Input number 2: '))
    except ValueError:
        ErrorNumber()
        continue
    else: 
        OddOrEven(number,number2,True)
        quit()