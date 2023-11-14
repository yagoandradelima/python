#Aula 06 - Desafio 004
a = input('digite algo: ')
print('O tipo primitivo dessa variável é {}'.format(type(a)))
#printando booleano para saber se a é só um espaço
print('Só tem espaços? ', a.isspace())
#printando booleano para saber se é só um espaço
print('É um número? ', a.isnumeric())
#printando booleano para saber se é só alfabeto
print('É alfabético? ', a.isalpha)
#printando booleano para saber se é alfanumérico
print('É alfanúmerico? ', a.isalnum())
#printando booleano para saber se é maiusculo
print('Está em maisúsculo? ', a.isupper())
#printando booleano para saber se é minusculo
print('Está em minúscula? ', a.islower())
#printando booleano para caso tenha uma inicial maiscúla
print('Está capitalizada? ', a.istitle())


