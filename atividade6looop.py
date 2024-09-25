while True:
    total = 0 
    nProduto = 1 
    
    while True: 
        Valor_produto = float (input(f"Produto {nProduto}: R$ ")) 
        if Valor_produto == 0: 
            break 
        else:
            total = total + Valor_produto 
            nProduto = nProduto + 1 

    print(f"Total: R$ {total}") 

    pagamento = float (input ("Dinheiro: R$")) 

    troco = pagamento - total 
    print(f"Troco: R$ {troco}") 