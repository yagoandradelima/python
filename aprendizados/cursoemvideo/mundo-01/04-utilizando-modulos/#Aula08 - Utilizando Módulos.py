"""
1 - COMANDO IMPORT importa todos comandos dentro da biblioteca selecionada.

1.1 - Caso eu queira importar um comando específico de uma biblioteca eu vou utilizar
o comando _FROM biblioteca IMPORT comando_

1.2 - É sempre muito importante ler a documentação de uma biblioteca

1.3 - Caso eu não defina o comando que importei eu devo utilizar a sintaxe:
_biblioteca.comando_. Caso eu defina o comando, basta utilizar ele normalmente
como _comando()_

"""

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')