#Aula14 - Desafio 064

#contador para mostrar no final quantos número foram digitados
c = 0

#input inicial do usuário
num = int(input('Digite um valor: '))

#força a soma a pegar o primeiro valor de num. Se não fizer isso, o primeiro valor inputado não entra na somatória final
soma = num

#while com consição de saída simples. Se num for igual a 999 ele para de rodar
while num != 999:
    #contador incrementando
    c += 1
    #input interno pra ficar rodando até o usuário digitar a condição de saída
    num = int(input('Digite um valor: '))
    #somatória dos valores inputados na repetição
    soma += num
    #condicional para remover o 999 da soma final
    if num == 999:
        #como o 999 é o último valor inputador (por ser o valor de saída), posso utilizar essa linha abaixo pra fazer com que a somatória subtraia o 999 automaticamente, mas também poderia ter digitado simplesmente no final {soma-999}
        soma -= num
print()
print(f'Você digitou {c} valores e a soma deles foi de {soma}!')
print()
print('Fim do Programa')
