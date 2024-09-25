def exibeMenu() :

    print ("##### MENU #####\n")

    print ("0- SAIR \n") 
    
    print ("1- SOMAR \n")
    
    print ("2- multiplicar \n")
    
    print ("3- subtrair \n")

    opcao = int (input ("Escolha uma opcao: "))

    return opcao

def somar (numero1, numero2) :
    resultado = numero1+numero2
    
    return resultado

def multiplicar (numero1, numero2) :
    resultado = numero1*numero2
    
    return resultado

def subtrair (numero1, numero2) :
    resultado = numero1-numero2
    

    return resultado

i=0

opcao=1

num1=0

num2=0

resultado=0

while opcao!=0:

    opcao = exibeMenu ()

    if opcao <= 0:
        break

    num1= float (input ("Informe o primeiro numero para a operacao: ") )

    num2= float (input ("Informe o segundo numero para a operacao: ") )

    if opcao == 1:

        resultado = somar (num1, num2)

        print ("Resultado: 8f\n\n" %resultado)

    if opcao == 2:

        resultado = multiplicar (num1, num2)

        print ("Resultado: 8f\n\n" %resultado)

    if opcao == 3:

        resultado = subtrair (num1, num2)

        print ("Resultado: %f\n\n" %resultado)