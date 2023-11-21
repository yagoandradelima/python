#Fazer o usuário criar uma lista e ao final, imprimir a primeira opção da lista

while True:
    array = []
    num = int(input('Digite o número a ser incluído no array: '))
    array.append(num)
    print(array)
    continuar = input('Deseja continuar[s/n]? ')
    
    if continuar == 'n':
        break

print('Código finalizado')
print(array[0])
