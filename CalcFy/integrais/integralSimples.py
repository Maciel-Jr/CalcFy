import random
from sympy import symbols, integrate
from auxiliar.positivoNegativo import positivoNegativo


#https://www.sympy.org/pt/features.html


def integraisSimples(quantidade,ativoResposta=False, ativoLimites=False):
    
    listaFuncao = []
    listaIntegral = []
    listaLimiteA = []
    listaLimiteB = []
    operacao = positivoNegativo()
    # Gere cálculos de integrais aleatórias
    for _ in range(quantidade):
        # Gere uma função aleatória
        
        Limite_a = random.randint(-5, 6)
        Limite_b= random.randint(-5, 6)

        x = symbols('x')
        a_coef = random.randint(-10, 10)
        b_coef = random.randint(-10, 10)
        c_coef = random.randint(-10, 10)
        expoente = random.randint(0, 6)


        if operacao == 'positivo':
            function = a_coef * x**2 + b_coef * x + c_coef
        else:
            function = a_coef * x**2 - b_coef * x + c_coef
        

        integrate(function, (x))


        if ativoLimites: integral = integrate(function, (x, Limite_a, Limite_b))
    
        listaFuncao.append(function)
        listaIntegral.append(integral)
        listaLimiteA.append(Limite_a)
        listaLimiteB.append(Limite_b)

    if ativoResposta == True:
        if ativoLimites == True:
            return listaFuncao, listaIntegral, listaLimiteA, listaLimiteB
        else:
            return listaFuncao, listaIntegral 
    else:
        if ativoLimites == True:
            return listaFuncao,listaLimiteA, listaLimiteB
        else:
            return listaFuncao
       
       
        

print(integraisSimples(5, ativoResposta=True, ativoLimites=True))
