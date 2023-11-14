#Funcionando!

ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    usr = int(input('Digite um valor entre 0 e 20: '))

    while 0 > usr or usr > 20:
        usr = int(input('Valor inválido. Por favor, informe um valor de 0 a 20: '))
    else:
        print(f'Você digitou {ext[usr]}')
        break
print('fim da execução')

