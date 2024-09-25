
while True:
    op1 = input("digite um nome de usuario ")
    op2 = input("digite uma senha ")

    nome = []

    nome.append(op1)

    senha = []

    senha.append(op2)

    if nome == senha:
        print("erro")
    else:
        print("vc entrou")
        break