class Circulo:
        def __init__(self,raio,circunferencia):
                self.raio=raio
                self.circuferencia= circunferencia  

        def calc_raio (self):

                calc=float(input("Digite o valor do raio: "))
                a=round(3.14*calc**2)
                result=a
                print()
                print(f"A Área do circulo é: {result}")
                print("------------------------------")

        def calc_circuferencia(self):

                calc2=float(input("Digite o valor do raio para saber a circunferência: "))
                c= round(2*3.14*calc2)
                resultado=c

                print()
                print(f"O Calculo da Circunferência é:  {resultado}")
                print("--------------------------------------------")
                


circ1=Circulo(0,0)
circ1.calc_raio()
circ1.calc_circuferencia()
