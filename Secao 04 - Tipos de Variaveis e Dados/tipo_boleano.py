"""
Tipo Booleano

Álgebra Booleana, criada por Boole

Formada por duas constantes: Verdadeiro ou Falso

Em python: True -> Verdadeiro, False - > Falso  OBS: Sempre com inicial maiúscula

Exemplos:

############## Como construir #################

ativo = True

print(ativo)


############## Operações básicas #################

# Negação (not): Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
    se for falso o resultado será verdadeiro. Ous seja sempre o contrário.

ativo = False

print(not ativo)


# Ou (or): É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro

True or True -> True

True or False -> True

False ou True -> True

False ou False -> False

######## Exemplo ########
ativo = True

logado = False

print(ativo or logado)


# E (and): Também é uma operação binaria, ou seja, depende de dois valores. Ambos devem ser verdadeiros

True or True -> True

True or False -> False

False ou True -> False

False ou False -> False

######## Exemplo ########
ativo = True

logado = False

print(ativo or logado)
"""


# Comprovação

5 > 6

5 > 6

6 == 6

4 <= 5


num1 = 7
num2 = 8

num1 > num2


num1 < num2 and num1 > 3