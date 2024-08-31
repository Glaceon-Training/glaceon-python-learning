# This function add number
def add(x, y):
    return x + y


# This function subtract number
def subtract(x, y):
    return x - y


# This function multiply number
def multiply(x, y):
    return x * y


# This function divide number
def divide(x, y):
    return x / y


print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

num1 = None
num2 = None

while True:
    # take input from user
    choice = input('Enter choice: ')

    # check if choice true
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        except ValueError:
            print('Invalid input, please enter a number')
            continue

    if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))

    if choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))

    if choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))

    if choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))

    # check if user wants another calculation
    # break while loop if answer is no
    next_calculation = input('Do you want to try another calculation? (yes/no): ')
    if next_calculation == 'no':
        print('Let us call it a day!')
        break
    else:
        print('Select operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
