def duplicate_count(text):
    lista = list(text.lower())
    contador = resposta = 0
    for elemento in lista:
        if lista.count(elemento) > contador:
            contador = lista.count(elemento)-1
            if contador > 0:
                resposta += 1
                lista.remove(elemento)
            else:
                continue
        else:
            continue
    print(resposta)

duplicate_count('Indivisibilities')