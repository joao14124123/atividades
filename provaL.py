print("Bem-vindo!!")

# Produtos
produtos_alimentos = [
    {"nome": "Steak", "preco": 0.75, "quantidade": 0},
    {"nome": "Nuggets Frango Congelado 1.5kg", "preco": 20.00, "quantidade": 0},
    {"nome": "Picanha 1kg", "preco": 58.99, "quantidade": 0},
    {"nome": "Coca-cola 2l", "preco": 8.89, "quantidade": 0},
    {"nome": "Budweiser 330ml", "preco": 4.00, "quantidade": 0}]

produtos_higiene = [
    {"nome": "Sabonete Francis 90g", "preco": 4.70, "quantidade": 0},
    {"nome": "Shampoo Tresemme 400ml", "preco": 18.00, "quantidade": 0},
    {"nome": "Condicionador Tresemme 400ml", "preco": 23.00, "quantidade": 0} ]

carrinho = []

while True:
    print("Selecione a opção abaixo:")
    print("[C] Cliente")
    print("[F] Funcionário")

    op = input("Digite aqui: ")

    nome = ""
    cpf = ""

    if op == "C" or op == "c":
        print("Bem-vindo, cliente!")
        while True:
            print("[1] Entrar")
            print("[2] Fazer cadastro")

            op_c = input("Digite aqui: ")

            if op_c == "2":
                c1 = input("Digite seu nome: ")
                c3 = input("Digite seu CPF sem caracteres: ")

                nome = c1
                cpf = c3

                print("Cadastro realizado")

            elif op_c == "1":
                N1 = input("Digite seu nome: ")
                C1 = input("Digite seu CPF sem caracteres: ")

                if N1 == nome and C1 == cpf:
                    print("Acesso permitido.")

                    while True:
                        print("Menu")
                        print("[1] Carrinho")
                        print("[2] Seções")
                        print("[3] Retirar produtos do carrinho")
                        print("[4] Pagar")
                        op_c2 = input("Digite aqui: ")

                        if op_c2 == "1":
                            if carrinho == []:
                                print("Seu carrinho está vazio.")
                            else:
                                total = 0
                                print("Seu carrinho:")
                                for i in range(len(carrinho)):
                                    print(f"{carrinho[i]['nome']}: {carrinho[i]['quantidade']} x R$ {carrinho[i]['preco'] }")
                                    total += carrinho[i]['quantidade'] * carrinho[i]['preco']
                                print(f"Total: R$ {total }")

                        elif op_c2 == "2":
                            print("Digite o número à esquerda para ir à seção que deseja")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            op_secao = input("Digite aqui: ")

                            if op_secao == "1":
                                print("Seção de Alimentos:")
                                i = 0
                                while i < len(produtos_alimentos):
                                    print(f"{i + 1} {produtos_alimentos[i]['nome']}: R$ {produtos_alimentos[i]['preco'] } Quantidade: {produtos_alimentos[i]['quantidade']}")
                                    i += 1

                                produto_escolhido = int(input("Digite o numero do produto para adicionar ao carrinho ou 0 para voltar: ")) - 1
                                if produto_escolhido != -1:
                                    quantidade = int(input(f"Digite a quantidade de {produtos_alimentos[produto_escolhido]['nome']} para adicionar ao carrinho: "))

                                    for item in carrinho:
                                        if item["nome"] == produtos_alimentos[produto_escolhido]["nome"]:
                                            item["quantidade"] += quantidade
                                            break
                                    else:
                                        carrinho.append({"nome": produtos_alimentos[produto_escolhido]["nome"], "preco": produtos_alimentos[produto_escolhido]["preco"], "quantidade": quantidade})

                                    print(f"{quantidade}x {produtos_alimentos[produto_escolhido]['nome']} adicionados ao carrinho.")

                            elif op_secao == "2":
                                print("Seção de Higiene:")
                                i = 0
                                while i < len(produtos_higiene):
                                    print(f"{i + 1}. {produtos_higiene[i]['nome']}: R$ {produtos_higiene[i]['preco'] } Quantidade: {produtos_higiene[i]['quantidade']}")
                                    i += 1

                                produto_escolhido = int(input("Digite o número do produto para adicionar ao carrinho ou 0 para voltar: ")) - 1

                                if produto_escolhido != -1:
                                    quantidade = int(input(f"Digite a quantidade de {produtos_higiene[produto_escolhido]['nome']} para adicionar ao carrinho: "))

                                    for item in carrinho:
                                        if item["nome"] == produtos_higiene[produto_escolhido]["nome"]:
                                            item["quantidade"] += quantidade
                                            break
                                    else:
                                        carrinho.append({"nome": produtos_higiene[produto_escolhido]["nome"], "preco": produtos_higiene[produto_escolhido]["preco"], "quantidade": quantidade})
                                    print(f"{quantidade}x {produtos_higiene[produto_escolhido]['nome']} adicionados ao carrinho.")

                            else:
                                print("Seção inválida")

                        elif op_c2 == "3":
                            print("Retirar produtos do carrinho:")
                            if carrinho == []:
                                print("Seu carrinho está vazio.")
                            else:
                                for i in range(len(carrinho)):
                                    print(f"{i + 1}. {carrinho[i]['nome']}: {carrinho[i]['quantidade']} x R$ {carrinho[i]['preco'] }")

                                produto_escolhido = int(input("Digite o número do produto para retirar do carrinho ou 0 para voltar: ")) - 1

                                if produto_escolhido != -1:
                                    quantidade = int(input(f"Digite a quantidade de {carrinho[produto_escolhido]['nome']} para retirar do carrinho: "))

                                    if quantidade >= carrinho[produto_escolhido]["quantidade"]:
                                        print(f"Todo o {carrinho[produto_escolhido]['nome']} foi removido do carrinho.")
                                        carrinho.pop(produto_escolhido)
                                    else:
                                        carrinho[produto_escolhido]["quantidade"] -= quantidade
                                        print(f"{quantidade}x {carrinho[produto_escolhido]['nome']} foram removidos do carrinho.")

                        elif op_c2 == "4":
                            if carrinho == []:
                                print("Seu carrinho está vazio.")
                            else:
                                total = 0
                                print("Seu carrinho:")

                                for item in carrinho:
                                    print(f"{item['nome']}: {item['quantidade']} x R$ {item['preco'] }")

                                    total += item['quantidade'] * item['preco']

                                imposto_nacional = total * 0.05
                                imposto_estadual = total * 0.08
                                imposto_municipal = total * 0.12
                                total_impostos = imposto_nacional + imposto_estadual + imposto_municipal
                                total_com_impostos = total + total_impostos

                                print(f"Total: R$ {total }")
                                print(f"Imposto Nacional (5%): R$ {imposto_nacional:.2f}")
                                print(f"Imposto Estadual (8%): R$ {imposto_estadual:.2f}")
                                print(f"Imposto Municipal (12%): R$ {imposto_municipal:.2f}")
                                print(f"Total de Impostos: R$ {total_impostos:.2f}")
                                print(f"Total com Impostos: R$ {total_com_impostos:.2f}")
                                print("Qual a forma de pagamento ?")
                                print("[1] Dinheiro [2] Pix [3] Cartão")
                                op_c3 = str(input("Digite aqui: "))

                                if op_c3 == "1":
                                    valor_entregue = float(input("Digite o valor entregue: "))
                                    if valor_entregue > total_com_impostos:
                                        troco = valor_entregue - total_com_impostos
                                        print(f"Compra realizada com sucesso!! Seu troco é R$ {troco:.2f}")
                                        carrinho = []
                                    elif valor_entregue == total_com_impostos:
                                        print("Compra realizada com sucesso!! Sem troco.")
                                        carrinho = []
                                    else:
                                        print("Valor insuficiente tente outra forma de pagamento")

                                elif op_c3 == "2":
                                    saldo_pix = float(input("Digite o saldo disponível no Pix: "))
                                    if saldo_pix >= total_com_impostos:
                                        print("Compra realizada com sucesso!!")
                                        carrinho = []
                                    else:
                                        print("Saldo insuficiente tente outra forma de pagamento")

                                elif op_c3 == "3":
                                    print("[1] Debito [2] Credito [3] Voucher")
                                    op_p = str(input("Digite aqui: "))
                                    saldo_cartao = float(input("Digite o saldo disponível no cartão: "))
                                    if saldo_cartao >= total_com_impostos:
                                        print('')
                                        print("Compra realizada com sucesso!")
                                        carrinho = []
                                    else:
                                        print("Saldo insuficiente tente outra forma de pagamento.")

                                else:
                                    print("Opção invalida.")

                                print("Nota Fiscal ")
                                print(f"Cliente: {nome}")
                                print(f"CPF: {cpf}")
                                for item in carrinho:
                                    print(f"{item['nome']}: {item['quantidade']} x R$ {item['preco']:.2f}")
                                print(f"Total: R$ {total:.2f}")
                                print(f"Imposto Nacional (5%): R$ {imposto_nacional:.2f}")
                                print(f"Imposto Estadual (8%): R$ {imposto_estadual:.2f}")
                                print(f"Imposto Municipal (12%): R$ {imposto_municipal:.2f}")
                                print(f"Total de Impostos: R$ {total_impostos:.2f}")
                                print(f"Total da Compra: R$ {total_com_impostos:.2f}")

                        else:
                            print("Opção invalida")
                else:
                    print("Acesso negado")
#funcionario

    elif op == "F" or op == "f":
        print("Bem vindo, funcionário!")

        produtos_alimentos = [
            {"nome": "Steak", "preco": 0.75, "quantidade": 0},
            {"nome": "Nuggets Frango Congelado 1.5kg", "preco": 20.00, "quantidade": 0},
            {"nome": "Picanha 1kg", "preco": 58.99, "quantidade": 0},
            {"nome": "Coca-cola 2l", "preco": 8.89, "quantidade": 0},
            {"nome": "Budweiser 330ml", "preco": 4.00, "quantidade": 0}
        ]

        produtos_higiene = [
            {"nome": "Sabonete Francis 90g", "preco": 4.70, "quantidade": 0},
            {"nome": "Shampoo Tresemme 400ml", "preco": 18.00, "quantidade": 0},
            {"nome": "Condicionador Tresemme 400ml", "preco": 23.00, "quantidade": 0}
        ]

        matricula = ""
        nome = ""
        data_nascimento = ""
        cpf = ""

        while True:
            print("[1] Entrar")
            print("[2] Fazer cadastro")

            op_f = str(input("Digite aqui: "))

            if op_f == "2":
                print("Sua matrícula é: 123")
                c1 = input("Digite seu nome : ")
                c2 = input("Digite sua data de nascimento sem caracteres: ")
                c3 = input("Digite seu CPF sem caracteres: ")

                matricula = "123"
                nome = c1
                data_nascimento = c2
                cpf = c3

                print("Cadastro realizado")

            elif op_f == "1":
                M = input("Digite sua matrícula sem caracteres: ")
                N = input("Digite seu nome: ")
                D = input("Digite sua data de nascimento sem caracteres: ")
                C = input("Digite seu CPF sem caracteres: ")

                if M == matricula and N == nome and D == data_nascimento and C == cpf:
                    print("Acesso permitido.")
                    while True:
                        print("[1] Consultar estoque")
                        print("[2] Atualizar estoque")
                        print("[3] Adicionar novos produtos ao estoque")
                        print("[4] Retirar produtos do estoque")
                        print("[5] Alterar preços dos produtos")
                        op_e = int(input("Digite aqui: "))

                        if op_e == 1:
                            print("Digite o número à esquerda para ir à seção que deseja")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            op_e2 = int(input("Digite aqui: "))

                            if op_e2 == 1:
                                print("Estoque de Alimentos:")
                                for i in range(len(produtos_alimentos)):
                                    print(f"{i + 1}. {produtos_alimentos[i]['nome']}: R$ {produtos_alimentos[i]['preco']:.2f} - Quantidade: {produtos_alimentos[i]['quantidade']}")
                            elif op_e2 == 2:
                                print("Estoque de Higiene:")
                                for i in range(len(produtos_higiene)):
                                    print(f"{i + 1}. {produtos_higiene[i]['nome']}: R$ {produtos_higiene[i]['preco']:.2f} - Quantidade: {produtos_higiene[i]['quantidade']}")
                            else:
                                print("Seção inválida")

                        elif op_e == 2:
                            print("Atualizar estoque:")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            secao = int(input("Digite o número da seção: "))

                            if secao == 1:
                                print("Escolha um produto da lista de Alimentos:")
                                for i in range(len(produtos_alimentos)):
                                    print(f"{i + 1}. {produtos_alimentos[i]['nome']}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                print("Deseja adicionar ou retirar quantidade?")
                                print("[1] Adicionar")
                                print("[2] Retirar")
                                acao = int(input("Digite a ação: "))

                                quantidade = int(input("Digite a quantidade: "))

                                if acao == 1:
                                    produtos_alimentos[produto_escolhido]["quantidade"] += quantidade
                                elif acao == 2:
                                    produtos_alimentos[produto_escolhido]["quantidade"] -= quantidade

                                    if produtos_alimentos[produto_escolhido]["quantidade"] < 0:
                                        produtos_alimentos[produto_escolhido]["quantidade"] = 0

                                print(f"Quantidade atualizada!! novo estoque de {produtos_alimentos[produto_escolhido]['nome']}: {produtos_alimentos[produto_escolhido]['quantidade']}")

                            elif secao == 2:
                                print("Escolha um produto da lista de Higiene:")

                                for i in range(len(produtos_higiene)):
                                    print(f"{i + 1}. {produtos_higiene[i]['nome']}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                print("Deseja adicionar ou retirar quantidade?")
                                print("[1] Adicionar")
                                print("[2] Retirar")
                                acao = int(input("Digite a ação: "))

                                quantidade = int(input("Digite a quantidade: "))

                                if acao == 1:
                                    produtos_higiene[produto_escolhido]["quantidade"] += quantidade

                                elif acao == 2:
                                    produtos_higiene[produto_escolhido]["quantidade"] -= quantidade

                                    if produtos_higiene[produto_escolhido]["quantidade"] < 0:

                                        produtos_higiene[produto_escolhido]["quantidade"] = 0

                                print(f"Quantidade atualizada!! novo estoque de {produtos_higiene[produto_escolhido]['nome']}: {produtos_higiene[produto_escolhido]['quantidade']}")

                            else:
                                print("Seção invalida quantidade não atualizada")

                        elif op_e == 3:
                            print("Adicionar novos produtos ao estoque: ")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            secao = int(input("Digite o numero da seção: "))

                        elif op_e == 4:
                            print("Remover produtos do estoque : ")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            secao = int(input("Digite o número da seção: "))

                            if secao == 1:
                                print("Escolha um produto da lista de Alimentos para remover:")
                                for i in range(len(produtos_alimentos)):
                                    print(f"{i + 1}. {produtos_alimentos[i]['nome']}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                produtos_alimentos.pop(produto_escolhido)
                                print("Produto removido da seção de alimentos com sucesso!!")
                                

                            elif secao == 2:
                                print("Escolha um produto da lista de Higiene para remover:")
                                for i in range(len(produtos_higiene)):
                                    print(f"{i + 1}. {produtos_higiene[i]['nome']}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                produtos_higiene.pop(produto_escolhido)
                                print("Produto removido da seção de Higiene com sucesso!")
                                

                            else:
                                print("Seção invalida produto não adicionado")
                                
                        elif op_e == 5:
                            print("Alterar preços dos produtos:")
                            print("[1] Alimentos")
                            print("[2] Higiene")
                            secao = int(input("Digite o número da seção: "))

                            if secao == 1:
                                print("Escolha um produto da lista de Alimentos para alterar o preço:")
                                for i in range(len(produtos_alimentos)):
                                    print(f"{i + 1}. {produtos_alimentos[i]['nome']}: R$ {produtos_alimentos[i]['preco']:.2f}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                novo_preco = float(input(f"Digite o novo preço para {produtos_alimentos[produto_escolhido]['nome']}: "))
                                produtos_alimentos[produto_escolhido]["preco"] = novo_preco
                                print(f"Preço atualizado!! Novo preço de {produtos_alimentos[produto_escolhido]['nome']}: R$ {produtos_alimentos[produto_escolhido]['preco']:.2f}")

                            elif secao == 2:
                                print("Escolha um produto da lista de Higiene para alterar o preço:")
                                for i in range(len(produtos_higiene)):
                                    print(f"{i + 1}. {produtos_higiene[i]['nome']}: R$ {produtos_higiene[i]['preco']:.2f}")
                                produto_escolhido = int(input("Digite o número do produto: ")) - 1

                                novo_preco = float(input(f"Digite o novo preço para {produtos_higiene[produto_escolhido]['nome']}: "))
                                produtos_higiene[produto_escolhido]["preco"] = novo_preco
                                print(f"Preço atualizad! Novo preço de {produtos_higiene[produto_escolhido]['nome']}: R$ {produtos_higiene[produto_escolhido]['preco']:.2f}")

                            else:
                                print("Seção invalida, preço não alterado.")
                        else:
                            print("Opção invalida.")
                else:
                    print("Acesso negado")
            else:
                print("Opção invalida!!")
    else:
        print("Opção invalida!!")