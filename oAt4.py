class aluno():
    nome = ""
    ra = "0"
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0

    def mostrarN (self):
        print(self.nome)

    def mostrarRa (self):
        print(self.ra)

    def calculo(self):
        soma = self.n1+self.n2+self.n3+self.n4 / 4
        if soma <=5:
            print("Reprovado")
        elif soma <=6.9:
            print("exame")
        else:
            print("aprovado")


def menu():
    print("\n MENU \n")
    print("(1) mostrar situaçao")
    print("(2) sair")
    print("(3) digite suas notas: ")

Aluno = aluno()

No= input("digite seu Nome: ")
while True:
    menu()

    op = float(input("digite suas notas: "))

    if op == 1:
        Aluno.calculo()
    elif op == 2:
        print("\n voce saiu \n")
        break
    elif op==3:
        Aluno.n1=(float(input("Digite a nota: ")))
        Aluno.n2=(float(input("Digite a nota: ")))
        Aluno.n3=(float(input("Digite a nota: ")))
        Aluno.n4=(float(input("Digite a nota: ")))