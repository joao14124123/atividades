import random

class Bingo:
    Nl=[]
    
    def __init__(self):
        self.servidor = {"B": [], "I": [], "N": [], "G": [], "O": []}

        self.marcados = {"B": [], "I": [], "N": [], "G": [], "O": []}
        self.gerar_tabelas()
        
    def sT(self):
        while True:
            
            sorteio = random.randint(1,75)
            if sorteio not in self.Nl:
                self.Nl.append(sorteio)
                print(f"\nnumero sortiado {sorteio}\n")
                
                
                return sorteio
                
            else:
                self.sT()


    def gerar_tabelas(self):
        for i in self.servidor:
            limite = 4 if i == "N" else 5
            while len(self.servidor[i]) < limite:
                if i == "B":
                    aleatorio = random.randint(1, 15)
                elif i == "I":
                    aleatorio = random.randint(16, 30)
                elif i == "N":
                    aleatorio = random.randint(31, 45)
                elif i == "G":
                    aleatorio = random.randint(46, 60)
                elif i == "O":
                    aleatorio = random.randint(61, 75)

                if aleatorio not in self.servidor[i]:
                    self.servidor[i].append(aleatorio)

        self.imprimir_tabelas()

    def imprimir_tabelas(self):
        for i , numbers in self.servidor.items():
            print(i , numbers)

    def marcar(self):
        op = int(input("digite o numero que quer marcar "))
        print()
            
            
            
            
        for i in self.servidor:
            if op in self.servidor['B']:
                self.marcados["B"].append(op)
                print(f"o numero {op} foi marcado! na tabela B\n")
                break

            elif op in self.servidor['I']:
                self.marcados["I"].append(op)
                print(f"o numero {op} foi marcado! na tabela I\n")
                break
                

            elif op in self.servidor['N']:
                self.marcados["N"].append(op)
                print(f"o numero {op} foi marcado! na tabela N\n")
                break
                

            elif op in self.servidor['G']:
                self.marcados["G"].append(op)
                print(f"o numero {op} foi marcado! na tabela G\n")
                break
                

            elif op in self.servidor['O']:
                self.marcados["O"].append(op)
                print(f"o numero {op} foi marcado! na tabela O\n")
                break
                
            else:
                print(f"o numero {op} nao esta em nenhuma tabela\n")
                print()
                break

    def bingo(self):
            for v in self.servidor:
                if len(self.marcados[v]) == 5:
                    print(f"Bingo na coluna {v}!")
                    return True

            for i in range(5):
                if (("B" in self.servidor and len(self.marcados["B"]) > i and self.servidor["B"][i] in self.marcados["B"]) and
                    ("I" in self.servidor and len(self.marcados["I"]) > i and self.servidor["I"][i] in self.marcados["I"]) and
                    ("N" in self.servidor and len(self.marcados["N"]) > i and self.servidor["N"][i] in self.marcados["N"]) and
                    ("G" in self.servidor and len(self.marcados["G"]) > i and self.servidor["G"][i] in self.marcados["G"]) and
                    ("O" in self.servidor and len(self.marcados["O"]) > i and self.servidor["O"][i] in self.marcados["O"])):
                    print(f"bingo na linha {i + 1}!")
                    return True
            return False

bingo = Bingo()

print("\n Bem vindo ao Bingo\n")

while True:


    print("[1] Marcar ")
    print("[2] Proximo Sorteio ")
    print("[3] Sair ")

    op2 = int(input("digite aqui: "))

    if op2 == 1:
        bingo.marcar()
        if bingo.bingo():
            print("Parabéns, você ganhou o Bingo!")
            break
    elif op2 == 2:
        bingo.sT()
    elif op2 == 3:
        print("voce saiu ")
        break
    else:
        print("opçao invalida, digite novamente")
        break