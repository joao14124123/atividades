carrinho = []
while True:
    print("menu")
    print("1 - produtaos")
    print("2 - visualisar o carrinho")
    print("3 - sair")
    
    op2 = int(input("digite a opção do menu"))
    
    if op2 == 3:
        break
    elif op2 == 2:
        print(f"produtos do carrinho {carrinho}")
    elif op2 == 1:
        print ("(E) lapis")
        print ("(R) borracha")  
        print ("(T) papel")
    
        op1 = input("digite o que quer colocar no carrinho ")
    
        if op1 == "E" or "e":
            carrinho.append("lapis")
        elif op1 == "R" or "r":
            carrinho.append("borracha")
        elif op1 == "T" or "t":
            carrinho.append("papel")
            
            
            