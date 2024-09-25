while True:
    nome = input("digite um nome com mais de 3 letras ")

    if nome == nome[0:3]:
        print("caracteres insuficientes")
    
    else:
        print("pode proseguir")
        break
    
while True:
    idade = int(input("digite sua idade (0 a 150) "))
    
    if idade <=0:
        print("idade invalida")
        
    elif idade >=150:
        print("idade invalida")
        
    else:
        print("pode proseguir")
        break
    
salario = int(input("digite seu salario "))
    
if salario >=0:
    print("valido")
else:
    print("invalido")
    
while True:
    
    print("informe seu sexo")
    print("(1) feminino")
    print("(2) masculino")
    print("(3) outro")
        
    inf = str(input("escolha uma das opçoes: "))

    
    if inf == "1":
        print("ok, feminino")
        break
    
    elif inf =="2":
        print("ok, masculino")
        break
    
    elif inf =="3":
        print("ok, outros")
        break
    
    else:
        print("digite uma opçao que seja 1,2 ou 3")
        

        
while True:
    print("informe seu estado civil")
    print("(1) solteiro")
    print("(2) casado")
    print("(3) viuvo")
    print("(4) divorciado")
    
    inf2 = str(input("escolha uma das opçoes: "))
    
    if inf2 == "1":
        print("ok, solteiro")
        break
    elif inf2 =="2":
        print("ok, casado")
        break
    elif inf2 =="3":
        print("ok, viuvo")
        break
    elif inf2 =="4":
        print("ok, divorciado")
        break
    else:
        print("digite uma opçao que seja 1,2,3 ou 4")