salario_atual = float(input("Digite o salário atual do colaborador: ")) 

if salario_atual <= 280: percentual_aumento = 20 

elif salario_atual <= 700: percentual_aumento = 15 

elif salario_atual <= 1500: percentual_aumento = 10 

else: percentual_aumento = 5 
aumento = salario_atual * (percentual_aumento / 100) 
novo_salario = salario_atual + aumento  
print("Salário antes do reajuste: R$", salario_atual)

print("Percentual de aumento aplicado:", percentual_aumento, "%") 

print("Valor do aumento: R$", aumento) 
print("Novo salário após o aumento: R$", novo_salario)