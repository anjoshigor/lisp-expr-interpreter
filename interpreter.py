
def interpreta(expr):
    return 17

def tokenize(expr):
    processed = expr.replace("("," ( ").replace(")"," ) ")
    tokens = processed.split()
    return tokens

def parse(tokens):
    tuplos = []
    stack = []
    for token in tokens:
        if(token == ")"):
            l = []
            tk = stack.pop()
            while(tk is not "("):
                l.append(tk)
                tk = stack.pop()
            
            if(stack == []):
                tuplos.append(tuple(l[::-1]))
            else:
                stack.append(tuple(l[::-1]))
            
            continue
        
        stack.append(conversion(token))
    
    return tuplos

VARS = {}
OPERANDS = ['*','+','-','/']
FUNC_DICT = {
            '*':lambda x,y: x*y,
            '+':lambda x,y: x+y,
            '-':lambda x,y: x-y,
            '/':lambda x,y: x/y,
            }

def avalia(tuplos):
    
    for tuplo in tuplos:        
        if(tuplo[0] == "define"):
            VARS[tuplo[1]] = tuplo[2]

    tup = [tuplo for tuplo in tuplos if tuplo[0] != "define"]

    r = avalia_recursive(tup[0],0)
    return r

def avalia_recursive(tuplo,i):
    tup = tuplo[i]

    if(tup in OPERANDS):
        return FUNC_DICT[tup](avalia_recursive(tuplo,i+1),avalia_recursive(tuplo,i+2))
    
    if(isinstance(tup,tuple)):
        return avalia_recursive(tup,0)
    
    if(isinstance(tup, int)):
        return tup
    
    return VARS[tup]
       

def interpreta(expr):
    tokens = tokenize(expr)
    tuples = parse(tokens)
    return avalia(tuples)

def conversion(token):
    if(token.isdigit()):
        return int(token)
    else:
        return token

def tests():
    expr = "(define x 5) (  + (* 2 x) 7)"
    assert tokenize(expr) == ['(', 'define', 'x', '5', ')' , '(', '+' , '(', '*' , '2', 'x', ')' , '7', ')' ]
    tokens = tokenize(expr)
    assert parse(tokens) == [ ( 'define', 'x', 5 ) , ( '+' , ( '*', 2 , 'x') , 7 ) ]
    tuplos = parse(tokens)
    assert avalia(tuplos) == 17

if __name__ == "__main__":
    tests()
    expr = "(define x 5) (define y 2) ( + (* 2 x) (* 5 y))"
    print(interpreta(expr))