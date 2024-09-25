numero = input("Digite um numero menor que 1000")

if(int(numero) > 1000):
    print("Numero invalido")
else:
    if(int(numero) >= 100):
        cent = int(numero[0])
        deze = int(numero[1])
        uni = int(numero[2])
        centTexto = "centenas"
        dezeTexto = "Dezenas"
        uniTexto = "Unidades"

        if(cent == 1):
            centTexto = "Centena"
        if(deze == 1):
            dezeTexto = "Dezena"
        if(uni == 1):
            uniTexto = "Unidade"
        
        print(f"{numero} = {cent} {centTexto}, {deze} {dezeTexto} e {uni} {uniTexto}")
    elif(int(numero) >= 10 and int(numero) < 99 ):
        deze = int(numero[0])
        uni = int(numero[1])
        dezeTexto = "Dezenas"
        uniTexto = "Unidades"
        if(deze == 1):
            dezeTexto = "Dezena"
        if(uni == 1):
            uniTexto = "Unidade"
        
        print(f"{numero} = {deze} {dezeTexto} e {uni} {uniTexto}")
    else:
        uni = int(numero)
        uniTexto = "Unidades"

        if(uni == 1):
            uniTexto = "Unidade"
        print(f"{numero} = {uni} {uniTexto}")
         