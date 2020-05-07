"""
Escopo de Variáveis

Quando falamos de variaveis temos 2 casos:

1 - Variaveis globais
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variaveis locais
    - Variaveis locais são reconhecidas apenas no bloco onde foram declarads, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variaveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor á mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 2
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)# Erro pois esta na local e não na global