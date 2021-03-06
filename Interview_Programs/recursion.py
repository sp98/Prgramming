'''
recursion to do a * b
'''

def mult(a, b):
    if a > 1:
        return b + mult(a-1, b)
    else:
        return b

print(mult(3, 5))


def factorial(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return a * factorial(a-1)

print(factorial(3))


def str_reversal(string):
    if string == "":
        return string
    else:
        return str_reversal(string[1:]) + string[0]

print(str_reversal('Santosh'))


fibTable = [0, 1]


def fibonacci(a):
    if a < 0:
        print('Invalid input')
    elif a <= len(fibTable):
        return fibTable[a-1]
    else:
        temp_fib = fibonacci(a-1) + fibonacci(a-2)
        fibTable.append(temp_fib)
        return temp_fib

print(fibonacci(300))
