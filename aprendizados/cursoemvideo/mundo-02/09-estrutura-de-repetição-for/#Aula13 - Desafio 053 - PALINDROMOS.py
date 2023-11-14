#Aula13 - Desafio 053

frase = str(input('Digite uma frase: ')).strip().lower()
#removendo os espaços de uma frase
palavras = frase.split()
#juntando as palavras sem espaços
junto = ''.join(palavras)
inverso = ''

#range passando reversamente pela frase
for i in range(int(len(junto)) - 1, -1, -1):
    #inverso armazenando os valores invertidos
    inverso += junto[i]

 
if inverso == junto:
    print('Isso é um palíndromo!')

else:
    print('Não é um palíndromo')


