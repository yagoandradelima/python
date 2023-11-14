#Aula09 - Desafio 027 - PRIMEIRO E ULTIMO NOME

nome = str(input('Digite um nome: ')).strip()

print(f'Primeiro nome = {nome.split()[0]}')
#O len começa a contar do número 1, enquanto a lista por padrão conta do número 0.
#O len serve para pegar todos os termos do nome independente do tamanho
#O -1 é pra que a contagem do len se acerte com a contagem da lista da frase. len começa sua contagem do 1 e a lista do 0.
#Se eu não fizer isso, dá o erro de que a lista está fora da indexação, pois o len está pegando uma unidade acima do valor de unidades da lista
a = len(nome.split()) - 1
print(f'Último nome = {nome.split()[a]}')

