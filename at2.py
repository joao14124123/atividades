ano = int(input("digite o ano em que vc nasceu  "))
ano2 = int(input("digite o ano atual  "))

idade = ano2 - ano
print ("a idade é " , idade)

if idade >=18:
    nome = input("digite seu nome ")
    print(f"{nome} sua entrada foi permitida ")
else:
    print("a sua entrada não é permitida por menor idade ")