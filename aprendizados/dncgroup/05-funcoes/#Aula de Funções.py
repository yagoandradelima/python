#Aula de Funções
    #criando uma função de imprimir
from tkinter import N


def ola():
    print('Olá Mundo!')
    print('---------')

    #criando uma funcao bem vindo
def bemvindo():
    print('-'*30)
    print('-'*12,'Bem-Vindo', '-'*12)
    print('-'*30)

    #criando um função com parâmetros
def bienvenido(frase):
    print('-'*30)
    print('-'*12,frase, '-'*12)
    print('-'*30)

def soma(a, b):
    s = a + b
    print(f'a soma é de {s}')

    #criando uma função com parâmetros opcionais
    #o primeiro parametro (a) jamais deve ficar vazio na hora de declaração, dá erro.
def soma1(a=0, b=0):
    s = a + b
    print(f'A soma é de {s}')

    #funcoes com retorno
def soma2(a=0, b=0):
    s = a + b
    return s #o retorno é basicamente uma maneira de você ter a variável da função com abertura pra trabalhar

    #funcao com parametros indefinidos
    #funcao de media
def media(*num):
    """
    A funçao de média calcula a média de vários números.
    Você deve colocá-los diretamente no valor
    A função não aceita lista nem dicionários
    num: são os números enviados, int ou float
    return: media = media dos números

    Versão 1.0
    """
    soma = 0
    qtd = len(num)
    for n in num:
        soma += n
    media = soma / qtd
    return media
    




print('Ação 1')
print('Pegar dados')
ola()
print()
#funcao bem vindo sendo chamada no codigo principal
bemvindo()

    #função com parametro de entrada
#txt = str(input('Digite a frase: '))
#bienvenido(txt)

soma (2, 5)
print()
soma1(8)
print()
#Se eu não tiver essa 'variável' puxando o valor, não aparece nada!
variavel = soma2(3, 8)
print(variavel)
print()
print()
var  = media(1,3,5,7,9)
print(f'{var:.2f}')

help(media)