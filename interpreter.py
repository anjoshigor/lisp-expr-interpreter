
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
operands = []
digits = []

def interpreta(tuplos):
    
    for tuplo in tuplos:        
        if(tuplo[0] == "define"):
            VARS[tuplo[1]] = tuplo[2]

    tup = [tuplo for tuplo in tuplos if tuplo[0] != "define"]

    avalia(tup)
    d = digits[::-1]

    while(operands != []):
        function = FUNC_DICT[operands.pop()]
        x = d.pop()
        y = d.pop()
        d.append(function(x,y))

    return d[0]
    


def avalia(lista):
    for tuplos in lista:
        for tup in tuplos:
            if(isinstance(tup,tuple)):
                avalia([tup])
            else:
                if(tup in OPERANDS):
                    operands.append(tup)
                elif(isinstance(tup, int)):
                    digits.append(tup)
                else:
                    digits.append(VARS[tup] )
       



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
    assert interpreta(tuplos) == 17

if __name__ == "__main__":
    tests()
