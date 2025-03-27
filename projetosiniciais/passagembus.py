precopassagem = (float(input("Digite o valor da passagem: ")))
idade = int(input("Digite a idade do passageiro: "))
estudante = str(input("O passageiro é estudante? (sim ou não)"))

if idade > 60:
    print("O valor da passagem é de R$",(0))
    print("O passageiro é isento de pagamento")
if estudante == "sim":
    print("O valor da passagem é de R$",(precopassagem/2))
else:
    print("O valor da passagem é de R$",(precopassagem))