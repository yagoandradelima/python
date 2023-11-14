#Aula09 - Desafio 026 - BUSCANDO LETRAS

frase = str(input('Digite uma frase: ')).strip()

print(len(frase))

print(f'A frase possui {frase.lower().count("a")} letras A')
print(f'A primeira letra A aparece na posição {frase.lower().find("a") + 1}')
print(f'A última letra A aparece na posição {frase.lower().rfind("a")+1}')
print()

#print(f'O último momento em que a letra minuscula aparece é na posição {frase.find("a",0,151)}')
#print(f'O último momento em que a letra maiuscula aparece é na posição {frase.find("A",len(frase))}')