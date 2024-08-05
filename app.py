from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

