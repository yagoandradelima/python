#Aula12 - Desafio 040 - MEDIA ESCOLAR

print('+'*33)
print(' '*9, '\033[1;37;40mMÉDIA ESCOLAR\033[m')
print('+'*33)
nota1 = float(input('Digite a primeira nota do Aluno: '))
nota2 = float(input('Digite a segunda nota do Aluno: '))
media = (nota1 + nota2)/2
print()
if media <= 5:
    print(f'Sua média foi {media:.2f}')
    print('\033[1;31;40mVOCÊ FOI REPROVADO\033[m')

elif media > 5 and media <= 6.9:
    print(f'Sua média foi {media:.2f}')
    print('\033[1;33;40mVOCÊ ESTÁ DE RECUPERAÇÃO\033[m')

else:
    print(f'PARABÉNS! Sua média foi de {media:.2f}')
    print('\033[1;32;40mVOCÊ ESTÁ APROVADO!\033[m')

print()
print('Fim do programa')