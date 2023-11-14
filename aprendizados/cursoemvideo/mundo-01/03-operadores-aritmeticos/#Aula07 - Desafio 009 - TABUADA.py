#Aula07 - Desafio 009
#O Desafio 9 é no puro print eu que decidi colocar while

print('=='*25)
print('=='*10, 'TABUADA', '=='*10)
print('=='*25)
num = int(input('Digite um número: '))
mult = 0
l = 0
print('=='*25)
print(f'TABUADA DE {num}')
while l < 10:
    l += 1
    mult = num * l
    #Usei o .format pra formatar melhor a exibição. Só executar e ver.
    print (' {} x {:>2} = {}'.format(num, l, mult))
    if l > 10:
        break
print('=='*25)
print('Fim do Código')
