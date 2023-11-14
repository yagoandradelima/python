#Aula14 - Desafio 066

c = soma = num = 0
continua = 'S' 

while continua == 'S':
    num = int(input('Digite um número: '))
    c += 1
    soma += num
    continua = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    if c == 1:
        maior = menor = num
    
    else:
        if num > maior:
            maior = num

        elif num < menor:
            menor = num
media = soma / c
print(f'A media dos valores digitados é: {media} \n O maior número digitado foi: {maior} \n O menor número digitado é: {menor}')
  