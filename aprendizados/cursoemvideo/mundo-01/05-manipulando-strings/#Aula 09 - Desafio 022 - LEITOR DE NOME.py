#Aula 09 - Desafio 022 - LENDO NOME
#Se eu definir a declaração da variável como str, posso usar as funções da aula 9 nela. Só observar como foi feito aqui com a variável nome

#strip eliminou possíveis espaços desnecessários que o usuário por inputar no ínicio ou no fim
nome = str(input('Digite seu nome completo: ')).strip()

qtd = int(len(nome.split()[0])) + int(len(nome.split()[1]))

print(f' Nome em letras maiúsculas: {nome.upper()} \n Nome em letras minúsculas: {nome.lower()} \n Quantidade de letras sem os espaços internos: {qtd} \n Quantidade de letras do primeiro nome: {len(nome.split()[0])}')


#Segunda maneira de encontrar a quantidade de letras do primeiro nome

#nome.find(' ')

#O find vai buscar o primeiro espaço vazio entre nomes, assim ele vai contar indiretamente os caracteres por onde ele passou.
#Como o primeiro nome é separado do segundo por um espaço, os caracteres indiretos que ele contou são os do primeiro nome