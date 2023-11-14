#Aula14 - Desafio 057

#Por algum motivo os operadores lógicos de diferença deixavam o while em loop infinito. Somente o NOT IN funcionou perfeitamente. Preciso ler mais sobre esse problema

sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()

while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()
    print('Tente novamente')
print('Sexo cadastrado com sucesso')