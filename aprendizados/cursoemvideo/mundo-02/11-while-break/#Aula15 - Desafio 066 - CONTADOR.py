soma = c = num = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'Foram digitados {c} números e a soma deles é igual a {soma}')