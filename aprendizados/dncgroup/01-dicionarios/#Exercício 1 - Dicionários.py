#Exercício 1 - Dicionários

boletim = {}
alunos = []
contador = 0
sTotal = 0
mTotal = 0

while True:
    boletim['nome'] = str(input('Digite um nome: '))
    boletim['nota1'] = float(input('Digite a primeira nota: '))
    boletim['nota2'] = float(input('Digite a segunda nota: '))
    boletim['media'] = (boletim['nota1'] + boletim['nota2'])/2
    if boletim['media'] > 7:
        boletim['status'] = 'Aprovado'
    else:
        boletim['status'] = 'Reprovado'
    alunos.append(boletim.copy())
    contador += 1
    continua = input('Deseja continuar [s/n]? ')
    if continua == 'n':
        break
print()

#i está pegando os indices
#d está pegando os dicionários
#k está pegando as chaves dentro dos dicionários
#v está pegando os valores de cada chave
for i, d in enumerate(alunos):
    print(f'O(A) aluno(a) {d["nome"]} tirou {d["nota1"]:.2f} na primeira prova e {d["nota2"]:.2f} na segunda prova. Sua situação na disciplina é {d["status"]}')
    for k, v in d.items():
        if k == 'media':
            sTotal += d['media']
            mTotal = sTotal/contador

print()
print(f'A média da turma foi: {mTotal:.2f}')
print()
print()