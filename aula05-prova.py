qtdAlunos = int(input("Digite a quantidade de alunos: "))
nota1 = 0
nota2 = 0
nota3 = 0
for aluno in range(0,qtdAlunos):
    aluno = input("Digite o nome do aluno:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        aprovacao = "Aprovado"
    else:
        aprovacao = "Reprovado"
    print(f"{aluno} > Notas: {nota1}; {nota2}; {nota3} > Média: {media} > {aprovacao}")
