"""
Recebendo dados dos usuarios

input() -> Todo dado recebido via input é do tipo String

####### Exemplo de print 'antigo' versao 2.x #######

# Entrada de dados
print("Qual seu nome?")
nome = input()# Input será a entrada de dados

print('Seja bem-vindo(a) %s' % nome)

print("Qual sua idade: ")
idade = input()

# Processamento

# Saída de dados
print('A %s tem %s anos' % (nome, idade))


####### Exemplo de print 'moderno' versao 3.x em diante #######

# Entrada de dados
print("Qual seu nome?")
nome = input()

print('Seja bem-vindo(a) {0}'.format(nome))

print("Qual sua idade?")
idade = input()

print('A {0} tem {1} anos'.format(nome, idade))



"""

####### Exemplo de print 'mais atual' #######

# Entrada de dados
print("Qual seu nome?")
nome = input()

print(f'Seja bem-vindo(a) {nome}')

print("Qual sua idade?")
idade = input()

print(f'A {nome} tem {idade} anos')


# int(idade) -> cast
# O cast éa conversão de um tipo de dado para outro
print(f'A {nome} nasceu em {2018 - int(idade)}')