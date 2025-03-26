lista_cadastro = ([])

nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
email = str(input("Digite o email: "))
senha = str(input("Digite a senha: "))
confirma_senha = str(input("Confirme a senha: "))

if senha == confirma_senha:
    lista_cadastro.append(nome)
    lista_cadastro.append(idade)
    lista_cadastro.append(email)
    lista_cadastro.append(senha)

    print("Cadastro realizado com sucesso!")
    print(lista_cadastro)
    
    dado_altera = (input("Deseja alterar algum dado?"))
    if dado_altera == "sim":
        dado_altera = (input("Qual dado você deseja alterar?"))
        if dado_altera == "nome":
            nome = str(input("Digite o novo nome: "))
            lista_cadastro[0] = nome
            print(lista_cadastro)
        elif dado_altera == "idade":
            idade = int(input("Digite a nova idade: "))
            lista_cadastro[1] = idade
            print(lista_cadastro)
        elif dado_altera == "email":
            email = str(input("Digite o novo email: "))
            lista_cadastro[2] = email
            print(lista_cadastro)
        elif dado_altera == "senha":
            senha = str(input("Digite a nova senha: "))
            confirma_senha = str(input("Confirme a nova senha: "))
            if senha == confirma_senha:
                lista_cadastro[3] = senha
                print(lista_cadastro)
            else:
                print("As senhas não conferem!")
        else:
            print("Dado não encontrado!")
    dado_consulta = (input("Deseja consultar algum dado do cadastro?"))
    if dado_consulta == "sim":
        dado_consulta = (input("Qual dado você deseja consultar?"))
        if dado_consulta == "nome":
            print(lista_cadastro[0])
        elif dado_consulta == "idade":
            print(lista_cadastro[1])
        elif dado_consulta == "email":
            print(lista_cadastro[2])
        elif dado_consulta == "senha":
            print(lista_cadastro[3])
        else:
            print("Dado não encontrado!")
    else:
        print("Cadastro finalizado!")