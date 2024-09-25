cadernos = 100
canetas = 100
lapis = 100
borrachas = 100
reguas = 100

while True:
    print("menu:")
    print("(E) entrar no estoque")
    print("(S) sair do estoque ")
    print("(R) relatorio")
    print("(X) Sair")
    

    
    print(" por favor digite a opção do (menu)")
    
    op = input("o que quer fazer? ")
    
    if op=="E" or op=="e" :
        
        cod = int(input("digite o codigo do produto "))
        quantidade = int(input("digite a quantidade "))


        if cod == 10:
            cadernos = cadernos + quantidade
            print(cadernos)
            
        if cod == 20:
            canetas = canetas + quantidade
            print(canetas)
            
        if cod == 30:
            lapis = lapis + quantidade
            print(lapis)
            
        if cod == 40:
            borrachas = borrachas + quantidade
            print(borrachas)
            
        if cod == 50:
            reguas = reguas + quantidade
            print(reguas)
    
    elif op == "S" or op=="s":
        
        cod = int(input("digite o codigo do produto "))
        quantidade = int(input("digite a quantidade "))

        if cod==10:
            cadernos=cadernos-quantidade
            print(cadernos)
    
        if cod == 20:
            canetas = canetas - quantidade
            print(canetas)
            
        if cod == 30:
            lapis = lapis - quantidade
            print(lapis)
            
        if cod == 40:
            borrachas = borrachas - quantidade
            print(borrachas)
            
        if cod == 50:
            reguas = reguas - quantidade
            print(reguas)
            
    elif op == "R" or op=="r":
        
        print(cadernos)
        print(canetas)
        print(lapis)
        print(borrachas)
        print(reguas)