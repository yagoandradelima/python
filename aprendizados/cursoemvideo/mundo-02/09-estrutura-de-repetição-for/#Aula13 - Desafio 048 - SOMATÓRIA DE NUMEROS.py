#Aula13 - Desafio 048

a = 0

#No código da atividade, ele colocou o range para pular de 2 em 2 já que a PA do range iniciando em 1 e progredindo em 2 sempre dá números ímpares. 

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        a += i
print(a)