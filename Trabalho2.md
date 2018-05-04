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