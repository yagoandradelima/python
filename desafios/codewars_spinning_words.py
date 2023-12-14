def spin_words(sentence):
    if sentence == '':
        return 'Nothing here'
    else:
        separado = sentence.split()
        resposta = ''
        for passo in separado:
            if len(passo) >= 5:
                resposta += f'{passo[::-1]} '
            else:
                resposta += f'{passo} '
        return resposta.stripe()

print(spin_words('bora com a gente no ônibus'))