
soma = 0 

while True:
    num = input()
    
    if int(num) >0:
        while num !="":
            soma = soma +int(num[0])
            num = num[1:]
    elif int(num) ==0:
        print(soma)
        break
    else:
        print("invalido")