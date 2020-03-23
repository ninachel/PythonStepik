a = float(input())
b = float(input())
operation = input()
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif operation == '*':
    print(a * b)
elif operation == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif operation == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
elif operation == 'pow':
    print(a ** b)
