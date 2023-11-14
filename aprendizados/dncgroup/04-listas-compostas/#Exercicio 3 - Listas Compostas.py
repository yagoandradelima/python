#Sinto esse exercício incompleto
#Ele não consegue puxar os dados de um usuário em uma posição fora do c
#O problema nesse código era o else ele fazia o código pegar outro rumo

cliente = []
cadastros = []
print(cadastros)
continua = 's'
continua1 = 's'

while continua == 's':
    cliente.append(str(input('Nome do cliente: ')))
    cliente.append(str(input('E-mail do cliente: ')))
    cliente.append(int(input('Telefone do cliente: ')))
    cliente.append(int(input('Idade do cliente: ')))
    cadastros.append(cliente[:])
    cliente.clear()
    continua = input ('Deseja continuar [s/n]? ')
    print()

while continua1 == 's':
    continua1 = input('Deseja iniciar a ferramenta de busca [s/n]? ')
    for c in cadastros:
        print('***FERRAMENTA DE BUSCA***')
        busca = input('Digite o e-mail do usuário: ')
        if busca in c:
                print(f'Nome do Cliente = {c[0]}')
                print(f'E-mail do Cliente = {c[1]}')
                print(f'Telefone do Cliente = {c[2]}')
                print(f'Idade do Cliente = {c[3]}')
                continua1 = input('Deseja continuar [s/n]? ')
#print(cliente)
print('Fim')