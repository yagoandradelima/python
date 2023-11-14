#Aula09 - Desafio 023 - DISSECANDO UM NÚMERO

#Fazer por string dá problema porquê toda vez que o número for menor que 4 dígitos, onde houver 0 o programa não vai reconhecer
#A maneira mais simples de funcionar está abaixo dele
num = str(input('Digite um número [4 dígitos necessários]: '))

print(f'Milhar: {num.strip[0]}')
print(f'Centenas: {num.strip[1]}')
print(f'Dezenas: {num.strip[2]}')
print(f'Unidades: {num.strip[3]}')

"""

Para pegar a unidade, basta pegar a divisão inteira por 1 e pegar o módulo dessa divisão por 10. E assim por diante.

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

"""