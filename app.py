from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produk')
def produk():
    return render_template('frontend/produk.html')

@app.route('/detail-produk')
def detail():
    return render_template('frontend/detail.html')

@app.route('/dashboards')
def dashboards():
    return render_template('frontend/dashboards.html')
