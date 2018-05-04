from math import sqrt,cos,sin

VARS = {}
BINARY_OPERANDS = ['*','+','-','/','<','>','eq','dif','>=','<=']
UNARY_FUNCTIONS = ['sqrt','cos','sin']
CONDS = ['if']
FUNC_DICT = {
            '*':lambda x,y: x*y,
            '+':lambda x,y: x+y,
            '-':lambda x,y: x-y,
            '/':lambda x,y: x/y,
            '<':lambda x,y: x<y,
            '>':lambda x,y: x>y,
            'eq':lambda x,y: x==y,
            'dif':lambda x,y: x!=y,
            '>=':lambda x,y: x>=y,
            '<=':lambda x,y: x<=y,
            'sqrt': sqrt,
            'cos': cos,
            'sin': sin
            }

def tokenize(expr):
    '''
    This function takes a string expression and returns a list of tokens
    '''
    #adding spaces around parenthesis
    processed = expr.replace("("," ( ").replace(")"," ) ")
    #splitting the string into a list
    tokens = processed.split()
    return tokens

def parse(tokens):
    '''
    This function takes a list of tokens and returns a list of tuples using the parenthesis for that
    '''
    #list for storing the result
    tuplos = []
    #a stack to deal with nested expressions
    stack = []

    for token in tokens:
        if(token == ")"):
            #auxiliar list
            l = []
            #pop from stack until a left parenthesis is reached
            tk = stack.pop()
            while(tk is not "("):
                l.append(tk)
                tk = stack.pop()

            #if the stack is empty, the tuple is appended to the result list in the reverse form
            if(stack == []):
                tuplos.append(tuple(l[::-1]))
            else:
                stack.append(tuple(l[::-1]))
            
            continue
        #if it's not a right parenthesis, just push into te stack
        stack.append(conversion(token))
    
    return tuplos

def avalia(tuplos):
    '''
    This function fills the VARS dictionary with the variables defined in the expression.
    Then, it removes the variables definition and pass the expression tuple to the recursive
    function to evaluate it
    '''
    for tuplo in tuplos:        
        if(tuplo[0] == "define"):
            VARS[tuplo[1]] = tuplo[2]

    tup = [tuplo for tuplo in tuplos if tuplo[0] != "define"]

    r = avalia_recursive(tup[0],0)
    return r

def avalia_recursive(tuplo,i):
    '''
    This is the main evaluation function. It takes a tuple and evaluates it
    in term of the kind of tuple is it. The tuple could be the following:
    
    1) An unary function such as: cos, sin, sqrt
    2) An if condition
    3) A binary operand such as: *, /, +, <
    4) An instance of a tuple
    5) A variable
    6) A value
    '''
    tup = tuplo[i]

    if(tup in UNARY_FUNCTIONS):
        return FUNC_DICT[tup](avalia_recursive(tuplo, i+1))

    if(tup in CONDS):
        if(avalia_recursive(tuplo,i+1)):
            return avalia_recursive(tuplo,i+2)
        else:
            return avalia_recursive(tuplo,i+3)
    
    if(tup in BINARY_OPERANDS):
        return FUNC_DICT[tup](avalia_recursive(tuplo,i+1),avalia_recursive(tuplo,i+2))
    
    if(isinstance(tup,tuple)):
        return avalia_recursive(tup,0)
    
    if(tup in VARS):
        return VARS[tup]

    return tup
       
def interpreta(expr):
    tokens = tokenize(expr)
    tuples = parse(tokens)
    return avalia(tuples)

def conversion(token):
    '''
    Simple conversion function to return the value of a digit and a string otherwise

    Ex: conversion('3') yields to 3
        conversion('x') yields to 'x'
    '''
    if(token.isdigit()):
        return int(token)
    else:
        return token

def tests():
    '''
    Function to test the expected value from the example provided by the assignment
    '''
    expr = "(define x 5) (  + (* 2 x) 7)"
    assert tokenize(expr) == ['(', 'define', 'x', '5', ')' , '(', '+' , '(', '*' , '2', 'x', ')' , '7', ')' ]
    tokens = tokenize(expr)
    assert parse(tokens) == [ ( 'define', 'x', 5 ) , ( '+' , ( '*', 2 , 'x') , 7 ) ]
    tuplos = parse(tokens)
    assert avalia(tuplos) == 17

if __name__ == "__main__":
    expr = "(define x 2) (if ( eq x (- 3 1)) (* (cos x) 10) (* x 4))"
    print(interpreta(expr))
