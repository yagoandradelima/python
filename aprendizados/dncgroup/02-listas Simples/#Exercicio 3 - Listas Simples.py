from webbrowser import Galeon


l1 = []
continua = 's'
cadProd = 0

while continua == 's':
    cadProd = input('Qual produto deseja inserir? ')
    #Não preciso fazer loop. O Not in me salva pra poder verificar valores existentes em uma lista
    if cadProd not in l1:
        l1.append(cadProd)
    else:
        print('Valor já existente. Cadastre um novo valor')
    continua = input('Deseja cadastrar um novo produto [s/n]? ')
print(l1)
print('Fim do programa')