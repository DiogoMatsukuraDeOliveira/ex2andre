from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

historico = []

@app.route('/')
def index():
    return render_template('index.html', historico=historico)

@app.route('/calcular', methods=['POST'])
def calcular():
    operacao = request.form['operacao']
    x = int(request.form['x'])
    y = int(request.form['y'])
    
    if operacao == 'soma':
        result = x + y
        historico.append(f"Soma: {x} + {y} = {result}")
    elif operacao == 'subtracao':
        result = x - y
        historico.append(f"Subtração: {x} - {y} = {result}")
    elif operacao == 'multiplicacao':
        result = x * y
        historico.append(f"Multiplicação: {x} * {y} = {result}")

    elif operacao == 'divisao_inteira':
        if y != 0:
            result = x // y
            historico.append(f"Divisão Inteira: {x} // {y} = {result}")
        else:
            result = "Erro: Divisão por zero"
            historico.append(result)

    return redirect(url_for('index'))

@app.route('/limpar_historico')
def limpar_historico():
    historico.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)