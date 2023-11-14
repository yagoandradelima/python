#Aula12 - Desafio 042 - DESAFIO DOS TRIÂNGULOS V2.0

"""

Um regra fundamental que aprendi aqui.

Se a == b e b == c, logo automaticamente o Python indica de a == c
PORÉM se o caso for a != b e b != c, o Python não indica que a != c, isso porque 'a' e 'c' podem ser iguais!

"""

r1 = float(input('Digite o valor do primeiro lado: '))
r2 = float(input('Digite o valor do segundo lado: '))
r3 = float(input('Digite o valor do terceiro lado: '))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('As retas podem formar um triângulo retângulo!')
    
    elif r1 == r2 == r3:
        print('As retas podem formar um triângulo equilátero!')
    
    else:
        print('As retas podem formar um triangulo isósceles!')

else:
    print('As retas não podem formar um triângulo!')

print()
print('Fim do Prgrama')