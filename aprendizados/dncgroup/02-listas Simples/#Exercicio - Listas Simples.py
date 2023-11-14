l2 = [3, 2, 5, 0, 0, 8, 3, 8, 8, 4, 0, 9, 7, 8, 9, 3, 6, 0, 1]
print(l2)
print()
print('A quantidade de termos que essa lista possui é: ',len(l2))
print()
print('Deletando todos os zeros da lista...')
l2.remove(0)
print()
for i in l2:
    if 0 in l2:
        l2.remove(0)
print(l2)
print('A quantidade de termos da nova lista é: ',len(l2))