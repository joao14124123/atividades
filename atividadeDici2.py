l = []
maior = 0
for i in range(2):
    d = {}
    d["nome"] = input("digite seu nome ")
    d["função"] = input("digite sua função ")
    d["salario"] = float(input("digite seu salario "))
    
    l.append(d)
    
    print(l)
    
    if d["salario"] > maior:
        maior = d ["salario"]
    
for pessoa in l:
    if pessoa["salario"] == maior:
        print(f"pessoa com maior salario é {pessoa["nome"]}")