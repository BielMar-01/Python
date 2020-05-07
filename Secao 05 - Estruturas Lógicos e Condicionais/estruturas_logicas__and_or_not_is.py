"""
Estruturas Lógicas: and, or, not, is

Operadores unários:
    - not

Operadores binários:
    - and
    - or
    - is


##### Regras de funcionamento: #####

Para o 'not', o valor do booleano é invertido, ou seja, ser for True vira False e vise e versa

Para o 'and' ambos os valores precisam ser True.

Para o 'or' pelomenos um tem que ser True.


##### Exemplo: #####

# Exemplo 1: and
ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# Exemplo 2: or
ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# Exemplo 3: not
ativo = True

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!'


# Exemplo 4: is
ativo = True

if ativo is True:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
"""

ativo = True

if ativo is True:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
