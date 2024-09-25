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
        h = self.Htrabalhadas
        print(h)
        
    def adicionarNome(self):
        self.nome = str(input("digite seu nome: "))
        self.sobreN = str(input("digite seu sobre nome: "))



f1 = funcionario("","",0.0,0.0)

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