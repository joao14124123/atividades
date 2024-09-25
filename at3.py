s = float(input("digite o seu salario "))
p = float(input("digite a prestaçao "))

Lprestaçao = s * 0.20

if s > Lprestaçao:
    print(" empréstimo não concedido ")
else:
    print(" empréstimo concedido")