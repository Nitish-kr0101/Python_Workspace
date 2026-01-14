def square(num):
    return num*num

def cube(num):
    return num * num * num

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)