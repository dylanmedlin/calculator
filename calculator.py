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
    global num1
    global num2
    operator = input('Enter operator: ')
    if operator == '+':
        return
    elif operator == '-':
        return
    elif operator == '*':
        return
    elif operator == '/':
        return
    elif operator == '^':
        return
    # enter 'clear' to set num1 and num2 to 0, then ask for num1 again
    elif operator == 'clear':
        num1 = 0
        num2 = 0
        getnum1()
        getoperator()
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
    elif operator == '^':
        num1 = num1 ** num2
        print('=', num1)
        getoperator()
        getnum2()
    else:
        print('Invalid Operator')
        getoperator()
