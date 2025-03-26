valoretanol = float(input("Digite o valor do litro do etanol: "))
valorgasolina = float(input("Digite o valor do litro da gasolina: "))

rendimentoetanol =  0.7
rendimentogasolina =  0.9    

if(valoretanol * rendimentoetanol < valorgasolina * rendimentogasolina):
    print("Abasteça com Etanol")
else:  
    print("Abasteça com Gasolina")