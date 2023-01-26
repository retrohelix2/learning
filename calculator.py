num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
expression = input("Addition +, Subtraction -, or multiplication* ? ")

if expression == '+':
    print(num1 + num2)
elif expression == '-':
    print(num1 -num2)
else:
    print(num1 * num2)