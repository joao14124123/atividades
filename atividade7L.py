lista = [1,2,3,8]

for i in range(5):
   lista.append(int(input("digite um numero inteiro")))
   
nova_lista = []
for i in lista:
    if i !=8:
        nova_lista.append(i)
        
print(nova_lista)