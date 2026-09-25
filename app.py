from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    dados = {
        'titulo': 'Sistema de Gestão',
        'subtitulo': 'Desenvolvido com Python e Flask',
        'versao': '1.0.0',
    }
    # O ** "desempacota" o dicionário em argumentos nomeados
    return render_template('index.html', **dados)


@app.route('/index',  methods=['GET', 'POST'])
def formulario():

    if request.method == 'GET':
            distancia = int(request.form['distancia'])
            dias = int(request.form['dias'])
            transport = request.form.get('transport', 'Nada enviado')
            km = int(request.form['km'])
            emissao = float(request.form['emissao'])
            faixa = request.form.get('faixa', 'Nada enviado')

            mult = (dias * km) * 0.10

# redirecionando para outra rota
# url_for chama a função, não a rota

            return redirect(url_for ('index_resultado', distancia = distancia, 
                                     dias = dias, transport = transport, km = km,
                                     mult = mult, emissao = emissao, faixa = faixa
                                    ))

    return render_template('index.html')

@app.route('/exibir')   
def exibir_resultado():

    distancia = request.args.get('distancia')
    dias = request.args.get('dias')
    transport = request.args.get('transport')
    km = request.args.get('km')
    emissao = request.args.get('emissao')
    faixa = request.args.get('faixa')
    mult = request.args.get('mult')
   

    return render_template('index.html', distancia = distancia, 
                                     dias = dias, transport = transport, km = km,
                                     mult = mult, emissao = emissao, faixa = faixa)


# SEMPRE TEM Q ESTAR NO FINAL

if __name__ == '__main__':
    app.run(debug=True)