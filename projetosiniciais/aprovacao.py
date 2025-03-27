media = float()
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

faltas = int(input("Digite a quantidade de faltas do aluno: "))
quantidadeaula = int(input("Digite a quantidade de aulas do semestre: "))
    
if(faltas > quantidadeaula * 0.25):
    print("Reprovado por faltas")
elif((nota1 + nota2) / 2 >= 6):
    print("Aprovado" + " " + str((nota1 + nota2) / 2))
else:
    media = (nota1 + nota2) / 2 < 6
    print("Reprovado por média")
