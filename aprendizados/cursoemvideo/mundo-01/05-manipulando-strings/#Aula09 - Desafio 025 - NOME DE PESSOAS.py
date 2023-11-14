#Aula09 - Desafio 025 - NOME DE PESSOAS
#Ele pediu resultado TRUE or FALSE, minha triagem é mais complexa, mas o resultado do que ele pediu não bate
#Preciso tornar o strip() padrão pra alguns inputs
nome = str(input('Digite o nome da pessoa: ')).strip()

print(f'Resultado da primeira triagem: {"silva" in nome.lower()}')