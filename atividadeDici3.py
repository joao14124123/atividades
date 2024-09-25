print("bem vindo ")

l = []
d = {}


while True:

    print("-----------------")

    print("Selecione a opção abaixo:")
    print("[C] entrar como Medico")
    print("[F] entrar como Cliente")

    print("------------------")

    op = input("Digite aqui: ")

    while True:
        if op == "C" or op == "c":
            print("Bem-vindo, Dr!")
                
            print("[1] Ver consultas")
            print("[2] liberar pacientes")
            print("[3] sair")
        
            op1 = int(input("digite aqui: "))
        
            if op1 == 1:
                    print(l)
                    
            elif op1 ==2:
                    if l==[] or d == {}:
                        print("Você nao tem pacientes")

                    else:
                        l.remove(d)
                        print("voce liberou o paciente")
                        
            elif op1 == 3:
                print(" voce saiu ")
                break
                
        elif op == "F" or op == "f":
            print("Bem-vindo")
            print("[E] marcar consulta")
            print("[V] verificar historico de consultas")
            print("[S] Sair")

            op2 = input("digite aqui ")
                

            if op2 == "E" or op2 == "e":
                for i in range(2):
                    d["nome"] = input("digite seu nome ")
                    d["cpf"] = input("digite seu cpf ")
                    d["idade"] = input("digite sua idade ")
                    d["horario"] = float(input("digite o horario desejado "))

                    l.append(d)
                    print("consulta marcada com sucesso")
                    break
                    
            elif op2 == "S" or op2 == "s":
                print("voce saiu")
                break
            
            elif op2 == "V" or op2 == "v":
                print(l)
                if d == ():
                    print("seu historico esta vazio")