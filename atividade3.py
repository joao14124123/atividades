print (" olá !!")
print (" informe seu salário abaixo ")

salarioAt = float(input(" qual seu salário atual "))



if salarioAt<500:
    reajuste = salarioAt * 0.15 + salarioAt
elif salarioAt<1000:
    reajuste = salarioAt * 0.10 + salarioAt
    
else:
    reajuste = salarioAt * 0.05 + salarioAt
    
print (f" seu salario atual é de {reajuste}")