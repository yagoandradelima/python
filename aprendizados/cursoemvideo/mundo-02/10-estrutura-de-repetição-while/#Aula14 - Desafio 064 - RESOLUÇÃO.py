#Aula14 - Desafio 064 - RESOLUÇÃO 

#O código está muito mais simplificado e decidi copiar ele como modelo

#Em uma linha 3 variáveis declaradas
soma = cont = num = 0

#num do lado de fora pois caso o primeiro numero seja 999 ele não entra nos incrementos e somas dentro do while e vai direto pra fora da condição de repetição
num = int(input('Digite um valor: '))

while num != 999:
    cont += 1
    soma += num
    #O num fica em último dentro do while pois caso o valor seja 999 ele já  coloca o código pra fora do while sem passar pelo contador e somatória novamente
    num = int(input('Digite um valor: '))
print(f'Você digitou {cont} valores e a soma deles foi de {soma}!')