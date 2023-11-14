#Aula13 - Desafio 055

a = 0

for i in range(0, 5):
    peso = float(input('Digite o peso da pessoa: '))
    #alinhando as variáveis pra iniciar o condicional
      
    if i == 0:
        maior = menor = peso

    elif peso < menor:
        menor = peso
    
    elif peso > maior:
        maior = peso
    
    else:
        #Deixei o else fazendo alguma coisa só pra ele não ficar triste kkkk
        print("Dados não computados")


print(f'O maior peso digitado foi {maior}KGs e o menor foi {menor}KGs')
