print("Bem vindo !!")

nota = int(input("digite uma nota entre 0 e dez "))

while True:
    if nota >=10:
        print("nota invalida")
    elif nota <=0:
        print("nota invalida")
        break
    
    nota1 = int(input("digite uma nota entre 0 e dez "))
    
    if nota1 <=10:
        print("ok, obrigado")
    elif nota1 >=0:
        print("ok, obrigado")
        
