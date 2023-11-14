#Exercício 2 - Dicionários
nota = []
boletim = {}
alunos = []
contador = 0
sTotal = 0
mTotal = 0

while True:
    boletim['nome'] = str(input('Digite um nome: '))
    nota1 = int(input('Qual foi a nota da primeira prova? '))
    nota2 = int(input('Qual foi a nota da segunda prova? '))
    nota.append(nota1)
    nota.append(nota2)
    boletim['nota'] = nota[:]
    boletim['media'] = (nota1 + nota2)/2
    if boletim['media'] > 7:
        boletim['status'] = 'Aprovado'
    else:
        boletim['status'] = 'Reprovado'
    contador += 1
    alunos.append(boletim.copy())
    nota.clear()
    continua = input('Deseja continuar [s/n]? ')
    if continua == 'n':
        break
print()
for i, d in enumerate(alunos):
    print(f'O(A) Aluno(a) {d["nome"]}, tirou nota {d["nota"][0]} na primeira prova e {d["nota"][1]} na segunda prova. Sua média foi {d["media"]} e seu status é {d["status"]}')
    print()
    for k, v in d.items():
        if k == 'media':
            sTotal += d['media']
            mTotal = sTotal/contador

print()
print()
print(f'A média total da turma foi: {mTotal}pts')
