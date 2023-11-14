#Aula13 - Desafio 056

b = 0
somaIdade = 0
maior = 0
menor = 0

for i in range(1, 5):
    nome = str(input(f'Digite o nome da {i}ª pessoa: ')).strip().lower()
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}ª pessoa [M/F]: ')).strip().upper()
    print()
    
    somaIdade += idade

    #Caso o primeiro valor seja o maior, o i == 0 armazena ele, já que ele só armazenará algum valor caso o elif mais abaixo seja executado
    if i == 0:
        maior = menor = idade
        n = nome

    elif sexo == 'F' and idade > 20:
        b += 1
        

    elif sexo == 'M' and idade > maior:
        maior = idade
        n = nome

mediaIdade = somaIdade / 4

print()
print(f'A Média de idade do grupo é {mediaIdade:.1f}')
print(f'O homem mais velho possui {maior} anos e tem o nome de {n.capitalize()}!')
print(f'Existem {b} mulheres acima de 20 anos')
print()
