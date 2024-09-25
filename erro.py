
print ("bem vindo ao cardapio do Burgão !!")

print ("cadapio")

print ("Cachorro Quente 100 R$ 11,20")

print ("Ovo Simples 101 R$ 8,30")

print ("Bauru com Ovo 102 R$ 11,50")

print ("Hambúrguer 103 R$ 16,20")

print ("Refrigerante 201 R$ 6,00")

print ("Suco 202 R$ 7,50") 

print ("Água Mineral 203 R$ 4,70")

cardapio = int(input("digite o codigo do produto "))

#valores

c = 11,20
o = 8,30
b = 11,50
h = 16,20
r = 6,00
s = 7,50
a = 4,70

a100 = "cachorro quente"
b101 = "Ovo Simples"
c102 = "Bauru com Ovo"
d103 = "Hambúrguer"
e201 = "Refrigerante"
f202 = "Suco"
g203 = "Água Mineral"

a1 = 100
b2 = 101
c3 = 102
d4 = 103
e5 = 201
f6 = 202
g7= 203

#-------

if cardapio == 100:
    se=input("ok, algo mais ? ")
    if se == ("sim"):
        input("o que mais vai querer ? ")
        if a1 == 100:
           print("ok")
        s1 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            print("ok")
            print(f"ok, seu pedido")
        if b2 == 101:
            print("ok")
        s2 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            print("ok")
        if c3 == 102:
               print("ok")
        s3 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            ("ok")
        if d4 == 103:
               print("ok")
        s4 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            ("ok")
        if e5 == 201:
            print("ok")
        s5 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            print("ok")
        if f6 == 202:
            print("ok")
        s6 = input("algo mais ? ")
        if se == ("sim"):
            input("o que mais vai querer ? ")
        else:
            print("ok")
        if g7 == 203:
            print("ok")
        else:
            print("ok")
    else:
        print("ok")
        print(f"seu pedido foi {cardapio}")