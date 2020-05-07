"""
Estruturas Condicionais: if, else, elif é a junção de (else if)

elif não existe nem em C nem e Java
"""

idade = 12

"""
# Estrutura condicional if, else em C
if (idade < 18) {
    printf("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos");
}else{
    printf("È menor de idade")
}
"""

"""
# Estrutura condicional if, else em Java
if (idade < 18) {
    Sytem.out.println("Menor de idade");
}else if(idade == 18){
    Sytem.out.println("Tem 18 anos");
}else{
    Sytem.out.println("È menor de idade")
}
"""

if idade < 18:
    print('Menor de idade')
elif idade ==18:
    print('Tem 18 anos')
elif idade > 60:
    print('Idoso')
else:
    print('Maior de idade')

