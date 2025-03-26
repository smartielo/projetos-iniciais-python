peso = float(input("Digite o seu peso(Kg): "))
altura = float(input("Digite a sua altura(m): "))

imc = peso / (altura ** 2)

print("O seu IMC é: ", imc)
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 34.9:
    print("Classificação: Obesidade Grau 1")
elif 35 <= imc < 39.9:
    print("Classificação: Obesidade Grau 2")
else:
    print("Classificação: Obesidade Grau 3 (Mórbida)")