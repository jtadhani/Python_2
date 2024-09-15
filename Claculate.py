import math
def Addition(a = 0,*args):
    '''This Function is for Addition of two or more numbers'''
    return a + sum(args)

def Subtraction(a = 0,*args):
    '''This Function is for Subtraction of two or more numbers'''
    return a - sum(args)

def Multiplication(a = 0,*args):
    '''This Function is for Multiplication of two or more numbers'''
    return a * sum(args)

def Division(a = 0,*args):
    '''This Function is for Division of two or more numbers'''
    if sum(args) == 0:
        return 0
    else:   
        return a / sum(args)

def Modulus(a = 0,*args):
    '''This Function is for Modulus of two or more numbers'''
    return a % sum(args)

def root(a = 0,*args):
    '''This Function is for Root of a number'''
    return math.sqrt(a)

def Square(a = 0,*args):
    '''This Function is for Square of a number'''
    return a * a

def sin(a = 0,*args):
    '''This Function is for Sin of a number'''
    return math.sin(a)

def cos(a = 0,*args):
    '''This Function is for Cos of a number'''
    return math.cos(a)

def tan(a = 0,*args):
    '''This Function is for Tan of a number'''
    return math.tan(a)

def cot(a = 0,*args):
    '''This Function is for Cot of a number'''
    return 1 / math.tan(a)

def log(a = 0,*args):
    '''This Function is for Log of a number'''
    return math.log(a)

def power(a = 0,*args):
    '''This Function is for Power of a number'''
    return a ** sum(args)

def factorial(a = 0,*args):
    '''This Function is for Factorial of a number'''
    return math.factorial(a)