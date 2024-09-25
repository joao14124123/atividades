while True:
    print("menu:")
    print("1 Multiplicaçao")
    print("2 Divisao")
    print("3 Adisao")
    print("4 Subtraçao")
    print("5 Sair")
    
    op = int(input("escolha a operaçao "))

    if op == 5:
        print("ok")
        break
    
    n1 = float(input("digite o primeiro numero "))
    n2 = float(input("digite o segundo numero "))

    if op==2:
        x=n1/n2
        print(x)
    else:
        if op==1:
            x=n1*n2
            print(x)
        else:
            if op==3:
                x=n1+n2
                print(x)
            else:
                op==4
                x=n1-n2
                print(x)