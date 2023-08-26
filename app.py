from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, url_for, flash, redirect
import json
import datetime
from database import Database
from model.produto import Produto

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = not True


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/listar')
def listar():
    database = Database()
    products = database.listarProdutos()
    
    return render_template('inventario/listar.html', products=products)


@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    
    if request.method == 'POST':
        print(request.form['formNomeProduto'])
        print(request.form['formPartNumber'])
        print(request.form['formLabelProduto'])
        print(request.form['formStartInventory'])
        
        database = Database()
        novoproduto = Produto(request.form['formNomeProduto'],
                              request.form['formPartNumber'],
                              request.form['formLabelProduto'],
                              request.form['formStartInventory'])
        database.cadastrarProduto(novoproduto)

    
    return render_template('cadastrar.html')

@app.route('/atualizar/<int:produto_id>', methods=["GET", "POST"])
def atualizar(produto_id):
    database = Database()
    produto = database.get_produto_por_id(produto_id)
    database = Database()
    if request.method == "POST":
        print('requeste ' + str(produto_id))
        print(produto)
        database.atualizarProduto(produto_id, request.form['formNomeProduto'], request.form['formPartNumber'], request.form['formLabelProduto'], request.form['formStartInventory'], produto)
        return redirect(url_for('listar'))                         
       
    return render_template('atualizar.html', produto=produto)

@app.route('/excluir/<int:produto_id>', methods=["GET", "POST"] )
def excluir(produto_id):
    print('requeste ' + produto_id)
    database = Database()
    database.excluir_produto(id)
    return redirect(url_for('listar'))

