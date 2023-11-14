#Aula10 - Desafio 033 - COMPARANDO NUMEROS

#Eu não consegui encontrar uma lógica pois não queria fazer diversas condicionais, mas nesse código condicionais diversas eram necessárias

#Isso, utilizando as ferramentas entregues na aula 10


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num2 and num3 < num1:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num2 and num3 > num1:
    maior = num3

print(f'O menor numero digitado foi {menor}')
print(f'O maior numero digitado foi {maior}')