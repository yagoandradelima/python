#Aula15 - Desafio 069
#O código correto está no outro arquivo de desafio 069
#contadores que designei
idF = qtdM = maior = 0

#Print do menu
print('-'*25)
print(' '*2, 'CADASTRE UMA PESSOA')
print('-'*25)

#Condicional com true pra executar até o break
while True:
        #variáveis e prints do cadastro
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-'*25) 
        continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        #Condicional para continuar executando
        if continua == 'S':
            if idade > 18:
                maior += 1
            #Por algum motivo esse contador não tá funcionando
            if idade < 20 and sexo == 'F':
                idF += 1
            if sexo == 'M':
                qtdM += 1
            else:
                continua == 'S'
        elif continua == 'N':
            break
        else:
            continua == 'S'
print('='*7, ' FIM DO PROGRAMA ', '='*7)
print(f'{maior} pessoa(s) é(são) maiore(s) de idade \n{qtdM} Homem(ns) foi(foram) cadastrado(s) \n{idF} Mulher(es) possui(possuem) menos de 20 anos')
