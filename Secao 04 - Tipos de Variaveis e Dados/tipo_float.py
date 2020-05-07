"""
Tipo Float

Pode ser conhecido por tipo real ou decimal como: 20.00.

Para saber o tipo de uma variavel e so colocar: print(type(variavel)).

As operações vão funcionar normalmente no float.


Exemplos:

# Errado do ponto de vista do float
valor = 1, 44 # Essa forma de escrita vai gerar uma tupla e não um float
print(valor) # Caso voce queira saber o tipo é só colocar type(valor) que vai resultará em tuple
print(type(valor))


# Certo do ponto de vista do float
valor1 = 1.44
print(valor1)
print(type(valor1)) # Esse type resultará em float

# É possivel isso vai ser uma dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Operações no float
valor = 1.44
valor + 1
print(valor)

# Podemos converter um float para um int,
# OBS: Ao converter valores float para inteiros, nós perdemos precisão
valor = 1.44
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
var = 1j
print(var)
print(type(var))

var = 1j ** 2
print(var)


OBS: O separador de casas decimais na programação é o .(ponto) e não a ,(virgula).
"""
