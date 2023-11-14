#Aula09 - Desafio 024 - NOME DE CIDADES

city = str(input('Digite o nome da sua cidade: ')).strip()


#O modo como eu fiz retorna TRUE para todo Santo dentro da variável city e ele quer somente o começo
#print(f'Resultado da primeira triagem: {"santo" in city.lower()}')

#O modo correto é aqui:

#O [:5] é porquê Santo só possui 5 caracteres e ele vai fatiar só o início da entrada
#O UPPER é pra padronizar o que foi digitado, assim, independente do input, ele pode pegar a palavra Santo
print(city[:5].upper() == 'SANTO')