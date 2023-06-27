import random
from sympy import symbols, integrate


def positivoNegativo():
    operacao = random.choice(['positivo', 'negativo'])
    return operacao

#https://www.sympy.org/pt/features.html


def integraisSimples(quantidade,ativoResposta=False, ativoLimites=False):
    
    operacao = positivoNegativo()
    # Gere cálculos de integrais aleatórias
    for _ in range(quantidade):
        # Gere uma função aleatória
        x = symbols('x')
        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        expoente = random.randint(0, 6)
        if operacao == 'positivo':
            function = a_coef * x**2 + b_coef * x + c_coef
        else:
            function = a_coef * x**2 - b_coef * x + c_coef
        if ativoResposta == True:
            if ativoLimites == True:
                Limite_a = random.randint(-5, 6)
                Limite_b= random.randint(-5, 6)
                integral = integrate(function, (x, Limite_a, Limite_b)) 
                print("Função:", function)
                print("Integral:", integral)
                print("Limite A:", Limite_a)
                print("Limite B", Limite_b)
                print()

            else:
                integral = integrate(function, (x))
                print("Função:", function)
                print("Integral:", integral)
                print()
        else:
            if ativoLimites == True:
                Limite_a = random.randint(-5, 6)
                Limite_b= random.randint(-5, 6)
                integral = integrate(function, (x, Limite_a, Limite_b)) 
                print("Função:", function)
                print()

            else:
                integral = integrate(function, (x))
                print("Função:", function)
                print()
       
       
        

integraisSimples(5, ativoResposta=True, ativoLimites=True)
