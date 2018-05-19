from math import sqrt,cos,sin
import warnings

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
    return ['(']+tokens+[')']
    
def parse(tokens):
    '''
     This function takes a list of tokens and returns a list of tuples using the parenthesis for that
    '''
    elem = tokens.pop(0)

    if (elem=="("):
        lista = []
        while (tokens[0] != ')'):
            lista.append(parse(tokens))
        
        tokens.pop(0)
        return tuple(lista)

    return conversion(elem)

def avalia(tuplos):
    '''
    This function fills the VARS dictionary with the variables defined in the expression.
    Then, it removes the variables definition and pass the expression tuple to the recursive
    function to evaluate it
    '''
    for tuplo in tuplos:
        if(tuplo[0] == "define"):
            try:
                var = tuplo[2]
                if(isinstance(var,int)):
                    VARS[tuplo[1]] = var
                else:
                    VARS[tuplo[1]] = avalia_recursive(tuplo[2],0)
            except IndexError as error:
                raise SyntaxError("Wrong definition Syntax! for \'{}\'".format(tuplo))
            
    tup = [tuplo for tuplo in tuplos if tuplo[0] != "define"]

    if (len(tup)==0):
        return "Void"
    
    results = [avalia_recursive(t,0) for t in tup]

    return results[0] if (len(results)==1) else results

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
        if(len(tuplo)>2):
            warnings.warn("Unused variable(s) \'{}\' for unary function \'{}\'".format(tuplo[i+2::],tup))

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

    if(isinstance(tup,int)):
        return tup
    
    raise ValueError('Variable \'{}\' not defined!'.format(tup))

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


if __name__ == "__main__":
    print("Expression interpreter assignment")
    print("Type \"#\" to exit")
    while(True):
        expression = input(">>>> ")

        if(expression == "#"):
            break
        
        ##for simpler expressions
        if(expression[0] != '(' and expression[-1] != ')'):
            expression = '('+expression+')'
        

        print(interpreta(expression))
