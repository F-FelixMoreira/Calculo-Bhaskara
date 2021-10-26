#Bhaskara
import math

def inserirVal():

    global a,b,c,delta

    a = float(input("\nInsira o valor de A: "))
    b = float(input("Insira o valor de B: "))
    c = float(input("Insira o valor de C: "))

    delta = b**2-4*a*c

    if a == 0 or delta < 0:
        
        print("\nA equação não possui raízes reais. Insira os valores novamente: ")
        inserirVal()

    else:

        calcularBhaskara()

def calcularBhaskara():

    x1 = (-b+ (math.sqrt (delta))) / (2*a)
    x2 = (-b- (math.sqrt (delta))) / (2*a)


    print("\nResultado x1: ", round(x1,4))
    print("Resultado x2: ", round(x2,4))

    reiniciarCalculo()

def reiniciarCalculo():

    resposta = input("\nDeseja fazer novos cálculos? Y/N")

    if resposta == "y":
        inserirVal()

    else: print("\n bye bye \n")


inserirVal()




