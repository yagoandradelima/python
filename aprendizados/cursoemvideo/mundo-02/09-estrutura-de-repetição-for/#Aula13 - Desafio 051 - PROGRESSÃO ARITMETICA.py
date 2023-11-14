#Aula13 - Desafio 051

num = int(input('Digite um número: '))
raz = int(input('Digite a razão da Progressão: '))

pa = num + raz

for i in range (0, 10):
    #Se eu não colocar o i = 0 pra printar num, ele não printa o primeiro fator
    if i == 0:
        print(num)
    else:
        print(pa)
        pa += raz

print('fim do programa')

#Uma PA também pode ser resumida no seguinte comando
# for i in range(0, 10, raz)