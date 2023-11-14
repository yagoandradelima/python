#Aula11 - Cores em Python

"""
Para representar uma cor em Python é necessário utilizar a seguinte sequencia de código

CODIGO ANSI para cor

\033[cod_estilo;cod_corTexto;cod_corFundom

Se cod_estilo estiver vazio ele está em 0

Se o código estiver vazio ele retorna para o padrão do terminal


STYLE            TEXT             BACK
0 none           30 white        40 white
1 bold           31 red          41 red
4 underline      32 green        42 green 
7 negative       33 yellow       43 yellow
                 34 blue         44 blue
                 35 violet       45 violet
                 36 blue         46 blue
                 37 gray         47 gray

O 40 no BACK é o mesmo que none
"""

print('\033[1;0;41mOlá Mundo!\033[m')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[7;30;40mOlá Mundo!\033[m')



