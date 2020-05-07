"""
Tipo String

Sempre que abrir com um tipo de aspa fechar com o mesmo tipo

Em python, um dado é considerado do tipo string que:
- Estiver entre áspas simples -> 'uma string', '234', 'a', 'Trues', '42.3'
- Estives entre áspas duplas -> "uma string", "234", "a", "Trues", "42.3"
- Estives entre áspas simples tripas -> '''uma string''', '''234''', '''a''', '''Trues''', '''42.3'''
"""
# - Estives entre áspas simples duplas triplas -> """uma string""", """234""", """a""", """Trues""", """42.3"""

"""
############# Exemplo: #############

nome = 'Geek University'
print(type(nome))

# Caso precise colocar uma aspa simples coloque a string inteira dentro de uma aspa dupla
nome = "Gina's Bar"
print(nome)
print(type(nome))

# O barra n serve para pular para a proxima linha
nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

# Deixando todas as letras maiusculas 
nome = 'Geek University'
print(nome.upper())

# Deixando todas as letras minusculo 
nome = 'Geek University'
print(nome.lower())

# Deixando dentro de uma lista de strings ['Geek', 'University']
nome = 'Geek University'
print(nome.split())

# Por baixo dos panos é assim que uma string é de fato 
['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
[ 0,    1,  2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14]

# O 0 porque quer começar no G e o 4 pois que ir ate o e onde o 4 não é incluido
nome = 'Geek University'
print(nome[0:4]) # Essa operação é chamada de Slice de string
print(nome[5:15])

# Transformações dentro das listas
nome = 'Geek University'
print(nome.split()[0]) # Isso vai gerar ['Geek', 'University'] onde Geek vai ser a posição 0 e o University a 1

# Invertendo a string
nome = 'Geek University'
print(nome[::-1]) # [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta

# Substituindo caracteres OBS: Tem que te dois parametros
nome = 'Geek University'
print(nome.replace('e', 'P'))
"""

# Testa isso pois e muito legal isso é um Palíndromo
texto = 'socorram me subindo onibus em marrocos'
print(texto)
print(texto[::-1])