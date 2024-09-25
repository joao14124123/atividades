while True: 
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ") 
    if username == password:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Cadastro bem-sucedido!") 
    break