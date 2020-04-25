# define variables
num1 = float()
num2 = float()
operator = str()

# define functions for user to enter variables
# also then confirms if they are valid inputs
def getnum1():
    try:
        global num1
        num1 = float(input('Enter number: '))
    except ValueError:
        print('Invalid Input')
        num1 = float(input('Enter number: '))
    except:
        print('An Unknown Error Has Occurred')


def getnum2():
    try:
        global num2
        num2 = float(input('Enter number: '))
    except ValueError:
        print('Invalid Input')
        num2 = float(input('Enter number: '))
    except:
        print('An Unknown Error Has Occurred')


def getoperator():
    global operator
    operator = input('Enter operator: ')
    if operator == '+':
        return
    elif operator == '-':
        return
    elif operator == '*':
        return
    elif operator == '/':
        return
    else:
        print('Invalid Operator')
        getoperator()


# Start calculator
# Asks user for initial numbers to calculate
getnum1()
getoperator()
getnum2()

# Continue to ask user for more calculations forever
while True:
    # Operations
    if operator == '+':
        num1 = num1 + num2
        print('=', num1)
        getoperator()
        getnum2()
    elif operator == '-':
        num1 = num1 - num2
        print('=', num1)
        getoperator()
        getnum2()
    elif operator == '*':
        num1 = num1 * num2
        print('=', num1)
        getoperator()
        getnum2()
    elif operator == '/':
        num1 = num1 / num2
        print('=', num1)
        getoperator()
        getnum2()
    else:
        print('Invalid Operator')
        getoperator()