notap1 = float(input("Digite a nota da P1: "))
notap2 = float(input("Digite a nota da P2: "))
notasatividades = float(input("Digite a nota das atividades: "))
notap1 = notap1 * 0.35
notap2 = notap2 * 0.35
notasatividades = notasatividades * 0.30
media = notap1 + notap2 + notasatividades
print("A média do aluno é: ", media)   

if media > 7:
    print("Aprovado")
else:
    print("Reprovado")
