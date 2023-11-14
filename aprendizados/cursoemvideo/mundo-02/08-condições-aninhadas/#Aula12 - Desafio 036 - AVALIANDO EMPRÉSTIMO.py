#Aula12 - Desafio 036 - AVALIANDO EMPRÉSTIMO

from time import sleep


print('='*33)
#Colocando uma variação de cores no início
print(' '*5,'\033[1;30;47mAVALIANDO EMPRÉSTIMO\033[m')
print('='*33)

valorCasa = float(input('Qual o valor da casa? '))
salarioComprador = float(input('Qual o salário do comprador? '))
anosPagamento = int(input('Em quantos anos será quitado? '))

#controle é para criar a variável de controle que aciona ou não o if
controle = salarioComprador * 0.3

#O pagamento é mensal, por isso tenho que transformar os anos em meses
meses = anosPagamento * 12 

#calculando as parcelas mensais
pagamentoMensal = valorCasa / meses


#Encorpando o código com uma espera
print('PROCESSANDO...')
sleep(2)
print()

if pagamentoMensal <= controle:
    #Colocando cores verdes para a frase aprovado
    print('\033[0;32;40mEmpréstimo Aprovado! \033[m')
    print(f'O valor do pagamento mensal será de R$ {pagamentoMensal:.2f}')

else:
    #Colocando cores vermelhas para a frase reprovado
    print('\033[1;31;40mEmpréstimo negado! Você não possui os critérios para aprovação!\033[m')

print()
print('Fim do Programa')
