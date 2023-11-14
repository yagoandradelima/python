#Aula10 - Desafio 035 - FORMANDO UM TRIANGULO

#A Condição de existência de um triângulo rege o seguinte conceito:  A soma de dois lados, é sempre menos que o terceiro lado

r1 = float(input('Digite o valor do primeiro lado: '))
r2 = float(input('Digite o valor do segundo lado: '))
r3 = float(input('Digite o valor do terceiro lado: '))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print('Essas retas podem formar um triângulo!')

else:
    print('Essas retas não podem formar um triângulo!')
print()
print('Fim do programa')