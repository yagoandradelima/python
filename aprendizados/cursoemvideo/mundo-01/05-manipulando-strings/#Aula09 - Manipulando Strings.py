#Aula09 - Manipulando Strings

frase = 'Curso em Vídeo Python'

#Dentro de uma frase, cada caracter é como se fosse um local de uma lista. eu posso fatiar a lista normalmente.

#Fatiando um único caractere
print(frase[6])
print()

#Fatiando um intervalo definido
print(frase[9:15])
print()

#Fatiando um intervalo com final 1 valor acima do máximo
print(frase[9:21])
print()

#Fatiando um intervalo sem início definido
print(frase[:9])
print()

#Fatiando sem final definido
print(frase[10:])
print()

#Fatiando com saltos durante o intervalo
#O número 2 significa quantos caracteres ele vai pular até o próximo print
print(frase[2:17:2])
print()

#Fatiando tudo com final indefinido e saltos
print(frase[7::3])
print()

#Desconbrindo o comprimendo de caracteres da frase
print(len(frase))
print()

#Printando um contador de determinado caracter
print(frase.count('o'))
print()

#Contagem em um intervalo fatiado
# o é a letra sendo procurada, 0 é o início e 13 o fim\
print(frase.count('o',0,13))
print()

#Encontrando uma cadeia de caractere(ou o que eu colocar no ())
#Ele retorna o primeiro número do intervalo onde começou o que eu procuro
#Se ele não encontrar, ele retorna -1 (não existe)
print(frase.find('deo'))
print()

#Questionamentos futuros para recursos de repetição
#Ele retorna booleano
'Curso' in frase

#Reposicionar e trocar
#Ele trocou Python por Android
#O replace só gera uma modificação, mas não muda efetivamente. Ele só irá mudar caso eu coloque _var = var.replace_
frase.replace('Python', 'Android')
print(frase)
print()

#transformando em maiusculo
print(frase.upper())

print()

#transformando em minusculo
print(frase.lower())
print()

#capitalize
#ele joga toda a frase em minuscula e a primeira letra da frase fica em maiusculo
print(frase.capitalize())
print()


#Cada inicial de palavra em maiuscula
print(frase.title())
print()

#Removendo espaços inuteis de uma string
frase1 = "   Aprenda Python  "
print(frase1)
print(frase1.strip())
print()


#removendo espaços inuteis do lado direito (os ultimos espaços)
print(frase1.rstrip())

#removendo espaços inuteis do lado esquerdo
print(frase1.lstrip())
print()

#dividindo a string onde houver espaços
#O split remove os espãos internos da frase pega as partes separadas e gera uma lista com elas
print(frase.split()) 
print(frase)
print()

#juntando as partes separadas
'-'.join(frase)
print(frase)
print()

#Para fazer um texto longo dentro do print é bom utilizar as três aspas

#No Python tudo é um objeto e por isso posso usar os _.métodos()_

#É possível combinar métodos com métodos como algo do tipo frase.upper().count('O') ou frase.lower().find('vídeo')


#contando a quantidade de caracteres
print(len(frase))
