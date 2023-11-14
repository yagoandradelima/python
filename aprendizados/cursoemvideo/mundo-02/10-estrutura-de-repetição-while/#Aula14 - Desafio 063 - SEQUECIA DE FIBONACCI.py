#Aula14 - Desafio 063

#Não está correto, ele só consegue pegar uma parte do código
#Minha estratégia não funciona pra fibonacci, vou tentar fazer sozinho depois

#Esse código não funciona e eu vou corrigir ele


#Não posso usar o range nesse código por 2 motivos. O primeiro é que, caso o range comece do zero, ele entra na condição de saída do While. Segundo que caso termos seja igual a 1, ele simplesmente não vai printar nada e vai direto pra condição de verdade do while no final do código!



#CORRIGI O CÓDIGO


#Fibonacci precisa ter essas duas variáveis declaradas, pois elas são as iniciais
t1 = 0
t2 = 1

#c vai ser meu controlador para que a quantidade de termos que o usuário digitar seja o limite que irá aparecer
c = 0

print('-' * 25)
print('Sequência de fibonacci')
print('-' * 25)
print(f'{t1} -> {t2}', end='')

#input do usuário
termos = int(input('\nQuantos termos a mais você quer mostrar? '))


#A primeira condicional do while é a condicional de saída do desafio. 0 só deve ser utilizado pra quebrar a repetição
while termos != 0:
    #O segundo while é para gerar a repetição do print
    while c <= termos:
        #primeira parte da lógica de fibonacci
        t3 = t1 + t2
        #print para ser repetido
        print(f'{t3} -> ', end='')
        #segunda parte da lógica de fibonacci
        t1 = t2
        t2 = t3
        #contador é incrementando, assim, quando ele passar da varuável termos, ele irá forçar o segundo while a parar a repetição de prints
        c += 1
    #zerei o contador pra que caso o usuário deseje mostrar mais termos, ele não já esteja incrementado com o valor anterior
    c = 0
    #segundo input que vale como condição de verdade para o primeiro while
    termos = int(input('\nQuantos termos a mais você quer mostrar? '))
print()
#declaração de código finalizado
print('Fim')
