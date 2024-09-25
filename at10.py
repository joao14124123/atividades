print("digite somente numeros inteiros")
n1 = int(input(" digite o primeiro numero "))
n2 = int(input(" digite o segundo numero "))


if n1 == n2:
    print("os numeros são iguais")
else:
    print("os numeros são diferentes")
    if n1 > n2: 
        print(f" o maior numero é {n1}")
        print(f" o menor numero é {n2}")
    else:
        print(f"o maior numero é {n2} ")
        print(f" o menor numero é {n1}")