#Aula de Funcoes - Escopo local e global
#o que está dentro de uma funcao é local
#o que está no código principal é global

from calendar import c

#Função de somar
def soma(a, b=0):
    #o c da funcao está se sobrepondo ao do principal por estar antecedendo a global
    global c
    s = a + b
    c = 8
    return s



#Código Principal
#declaracao de variaveis padrão
a = 5
b = 2
c = 3
#puxando a funcao
somado = soma(a, b)
#printando as variaveis do codigo principal
print(a, b, c)
#printando o resultado do somado
print(somado)