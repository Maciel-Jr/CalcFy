import random
from sympy import symbols, integrate


def positivoNegativo():
    operacao = random.choice(['positivo', 'negativo'])
    return operacao

#https://www.sympy.org/pt/features.html


def integrais1(quantidade,ativoResposta=False, ativoLimites=False):
    
    operacao = positivoNegativo()
   
    for _ in range(quantidade):
        
        x = symbols('x')
        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        d_coef = random.randint(-10, 10)
        e_coef = random.randint(-10, 10)
        f_coef = random.randint(-10, 10)
        expoente = random.randint(0, 6)
        if operacao == 'positivo':
            functionU = a_coef * x**expoente + b_coef * x + c_coef
            functionV = f_coef * x**expoente + e_coef * x + f_coef
        else:
            functionU = a_coef * x**expoente + b_coef * x + c_coef
            functionV = f_coef * x**expoente + e_coef * x + f_coef
        if ativoResposta == True:
            if ativoLimites == True:
                Limite_a = random.randint(0, 6)
                Limite_b= random.randint(-5, 5)
                integral = integrate(functionU, (x, Limite_a, Limite_b))*functionV + integrate(functionU, (x, Limite_a, Limite_b))*functionU
                print("Função:({})x({})".format( functionU, functionV))
                print("Integral:", integral)
                print("Limite A:", Limite_a)
                print("Limite B", Limite_b)
                print()

            else:
                integral = integrate(functionU, (x))*functionV + integrate(functionU, (x))*functionU
                print("Função:({})x({})".format( functionU, functionV))
                print("Integral:", integral)
                print()
        else:
            if ativoLimites == True:
                Limite_a = random.randint(-5, 6)
                Limite_b= random.randint(-5, 6)
                integral = integrate(functionU, (x, Limite_a, Limite_b)) 
                print("Função:({})x({})".format( functionU, functionV))
                print()

            else:
                integral = integrate(functionU, (x))
                print("Função:({})x({})".format( functionU, functionV))
                print()
       
       
        

integrais1(5, ativoResposta=True)
