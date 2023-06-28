from flask import Flask, jsonify, request
from integrais.integralSimples import integraisSimples


    
app = Flask(__name__)



@app.route('/api/integral/<quantidade>/<ativoResposta>/<AtivoLimites>', methods=['GET'])
def integral(quantidade, ativoResposta=False, AtivoLimites=False):

    quantidade = int(quantidade)
    ativoResposta = ativoResposta.lower() == 'true'
    AtivoLimites = AtivoLimites.lower() == 'true'

    quantidade = int(quantidade)
    resultado = integraisSimples(quantidade, ativoResposta, AtivoLimites)

    mensagem = {
        'Funcoes': resultado[0],
        'Resultado': resultado[1],
        'Limites Superiores': resultado[2],
        'Limites Inferiores': resultado[3]
    }

    return jsonify(mensagem)


if __name__ == '__main__':
    app.run(debug=True)
