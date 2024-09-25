class conta():
    def __init__(self, nome,cpf ,numero , saldo):
        self.nome=nome
        self.cpf=cpf
        self.saldo=saldo
        self.numero=numero
    
    def mostrar(self):
        print(self.nome)
        print(self.cpf)
        print(self.numero)
        print(self.saldo)
        
    def deposito(self):
        self.saldo=float(input("\ndigite o valor do deposito: "))    
    
    def sacar(self):
        self.saldo=self.saldo-(float(input("\ndigite o valor que deseja sacar: ")))
        
    def mostrarS(self):
        print(self.saldo)

while True:
    p1 = str(input("\n digite seu nome: "))
    p2 =int(input("digite seu cpf: "))
    break

t1 = conta(p1 , p2 , 2 , 0.0)


while True:
    
    print("\n(1) informações ")
    print("(2) depositar ")
    print("(3) sacar ")
    print("(4) imprimir saldo")
    
    op1 = int(input("\n digite aqui: "))
    
    if op1 == 1:
        t1.mostrar()
        
    
    if op1 == 2:
        t1.deposito()
        
    elif op1==3:
        t1.sacar()
        
    elif op1==4:
        t1.mostrarS()
    
    else:
        break

class funcionario():
    def __init__(self, nome,sobreN ,Htrabalhadas, Vh):
        self.nome=nome
        self.sobreN = sobreN
        self.Htrabalhadas=Htrabalhadas
        self.Vh=Vh
        
        
    def mostrarF(self):
        print(self.nome)
        print(self.sobreN)
        print(self.Htrabalhadas)
        print(self.Vh)
        
    def nomeC(self):
        print(self.nome,self.sobreN)
    
    def calcularH(self):
        c = self.Htrabalhadas * self.Vh
        print(c)
    
    def incrementarH(self):
        h = float(input("digite a qui "))
        self.Htrabalhadas = h
        print(h)
        
    def adicionarNome(self):
        self.nome = str(input("digite seu nome: "))
        self.sobreN = str(input("digite seu sobre nome: "))



f1 = funcionario("","",0,50)

while True:
    
    print("\n(1) informações ")
    print("(2) mostrar nome completo ")
    print("(3) saldo ")
    print("(4) horas adicionais")
    print("(5) Adicionar Nome e Sobrenome")
    
    opf1 = int(input("\n digite aqui: "))
    
    if opf1 == 1:
        f1.mostrarF()
        
    
    if opf1 == 2:
        f1.nomeC()
        
    elif opf1==3:
        f1.calcularH()
        
    elif opf1==4:
        f1.incrementarH()
        
    elif opf1==5:
        f1.adicionarNome()
    
    