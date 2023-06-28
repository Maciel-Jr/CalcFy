from integrais.integralSimples import integraisSimples
from Derivadas.derivadasSimples import derivadasSimples


integrais = integraisSimples(5, ativoResposta=True, ativoLimites=True)
derivadas = derivadasSimples(5, ativoResposta=True)

print(f"Função: {integrais[0]}")
print(f"Limites Superiores: {integrais[2]}")
print(f"Limites inferiores: {integrais[3]}")
print(f"Função Integrada: {integrais[1]}")