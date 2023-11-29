from flask import Flask, request, jsonify #importando as classes necessárias para a aplicação

app = Flask(__name__)

def calc_fatorial(n):
    if n==0:
        return 1
    else: 
        return n*calc_fatorial(n-1)

def calc_fibonacci(n):
    fibonacci = [0,1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci[:n+1]

@app.route('/calcular', methods=['POST']) #executa a função calcular quando o API recebe uma solicitação POST no endpoint '\calcular'
def calcular():
    data = request.get_json()
    operacao = data.get('operacao')
    numero = data.get('numero')

    #verificação da operação desejada
    if operacao == 'fatorial':
        resultado = calc_fatorial(numero)
    elif operacao == 'fibonacci':
        resultado = calc_fibonacci(numero)
    else: 
        return jsonify({'error': 'Operação não suportada'})
    
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)   #sem argumentos, utiliza a porta padrão 5000. 


