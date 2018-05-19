# Segundo Trabalho Prático de Laboratório de Programação:

O trabalho deve ser realizado individualmente ou em grupos de dois alunos. A resolução do trabalho tem que ser enviada até ao final do dia **20 de Maio** ao respectivo professor da turma (Mário Florido : amf@dcc.fc.up.pt ou João Silva: joaoms@joaoms.com) com o subject: Laboratório de Programação- Trabalho 2

É obrigatória a apresentação dos trabalhos na respectiva aula da semana de **21 a 25 de Maio**.


## Enunciado:

### Implemente em Python um interpretador de uma linguagem de expressões aritméticas com definição de variáveis. As expressões aritméticas deverão estar na notação prefixa (Ex: (* 2 6) ou (+ 5 x), e a definição de variáveis deverá ser feita por atribuições da forma (define x 5). O argumento do interpretador é uma string de expressões. Exemplo:

```python
expr = “(define x 5) ( + (* 2 x) 7)” 

print (interpreta(expr))
```

deverá dar como resultado **17**.

Divida a elaboração do trabalho na implementação das seguintes funções Python:

1) tokenize, que divide a string inicial numa lista de palavras. Exemplo:

Para a expressão `expr = “(define x 5) ( + (* 2 x) 7)”` 

**tokenize(expr)** deverá retornar a lista:

```python
['(', 'define', 'x', '5', ')' , '(', '+' , '(', '*' , '2', 'x', ')' , '7', ')' ]
```
2) parse, deverá ter como argumento uma lista de palavras (tokens) e retornar uma lista de tuplos que representam cada expressão. 

Exemplo: a função parse aplicada à lista  de tokens `['(', 'define', 'x', '5', ')' , '(', '+' , '(', '*' , '2', 'x', ')' , '7', ')' ]` deverá retornar a lista de tuplos:

```python
[ ( 'define', 'x', 5 ) , ( '+' , ( '*', 2 , 'x') , 7 ) ]
```

3) avalia, deverá ter como argumento a lista de tuplos retornada pelo parser e deverá retornar o resultado da avaliação das expressões.

Exemplo: a função **avalia** aplicada à lista de tuplos `[ ( 'define', 'x', 5 ) , ( '+' , ( '*', 2 , 'x') , 7 ) ]` deverá retornar o número 17.

Sugestão: para avaliar variáveis implemente uma tabela que associa variáveis ao seu valor. Essa tabela deverá ser actualizada por instruções define e usada para avaliar variáveis. Pode ser mantida como uma variável global e implementada como uma lista de pares (variável, valor) ou como um **dicionário**.

## Implementação

A implementação é estruturada pelos dicionários e funções abaixo

```python
##Main structures
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

##Main functions
def tokenize(expr)
def parse(tokens)
def avalia(tuplos)

```
`VARS`: É um dicionário que será preenchido à medida que variáveis são definidas dentro da expressão a ser testada ou do programa interativo

`BINARY_OPERANDS`: Operadores binários suportados pelo trabalho

`UNARY_FUNTIONS`: Funções _built in_ do python que recebem apenas um argumento suportadas neste trabalho

`CONDS`: Operadores condicionais suportados nesse trabalho

`FUN_DICT`: Dicionário que transforma a representação da função para a função propriamente dita e assim pode ser aplicada dentro de uma expressão

As funções `tokenize`, `parse` e `avalia` são implementadas de acordo com a especificação do trabalho

Antiga função de parse que utilizava uma stack:

## Como correr:

Simplesmente caminhe até o diretório raiz do projeto e faça:

```console
python interpreter.py
```

Será aberto uma simulação de uma shell onde você poderá rodar comandos como o exemplo abaixo:

```console
Expression interpreter assignment
Type "#" to exit
>>>> (+ 2 (* 2 4))   
10
>>>> (define x (+ 2 (* 2 4)))
Void
>>>> x   
10
>>>> (if (x > 0) (sin x) (cos x))
-0.5440211108893698
>>>> #
```

Expressões mais simples também podem ser realizadas sem parênteses, como:

```console
Expression interpreter assignment
Type "#" to exit
>>>> define simple 10
Void
>>>> simple
10
>>>> + simple 1
11
>>>> #
```

Se as expressões retornarem mais de um valor, uma lista de valores é retornada, como no exemplo:

```console
Expression interpreter assignment
Type "#" to exit
>>>> (define x 10) (+ x 1) (+ x 2) (+ x 3)
[11, 12, 13]
>>>> #
```

## Como testar:

Basta caminhar até o diretório raiz do projeto e fazer:

```console
python tests.py
```
Serão realizados **8** testes unitários que cobrem os tópicos do presente trabalho e o levantamento de exceções e warnings.

## Observações

A função parse atual não foi a primeira forma de implementação do trabalho. A abordagem recursiva atual mostra um código muito mais limpo e fácil de entender do que a versão da mesma função anterior:

```python
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
```

```
Desenvolvido por
Higor Araújo dos Anjos
up201711183@fc.up.pt
```