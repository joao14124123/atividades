print("digite somente numeros inteiros")
n1 = int(input("digite o primeiro numero "))
n2 = int(input("digite o segundo numero "))
n3 = int(input("digite o terceiro numero "))



nm = n1

if n2 > nm:
    mn = n2
    if n3 > nm:
        nm = n3
print("o maior numero é " , nm)