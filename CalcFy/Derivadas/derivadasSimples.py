import random
from sympy import symbols, diff
from ..outros.positivo_negativo import positivoNegativo

#https://www.sympy.org/pt/features.html
# Defina os limites do intervalo de integração
def derivadasSimples(quantidade,ativoResposta=False):
    
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
            function = a_coef * x**expoente + b_coef * x + c_coef
        else:
            function = a_coef * x**expoente - b_coef * x + c_coef


        if ativoResposta == True:
                integral = diff(function, (x))
                print("Função:", function)
                print("Derivada:", integral)
                print()
        else:
                integral = diff(function, (x))
                print("Função:", function)
                print()
       
       
        

derivadasSimples(5, ativoResposta=True)
