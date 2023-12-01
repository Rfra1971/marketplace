from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Aquí es donde mostrarías los productos artesanales disponibles
    return render_template('home.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    # Aquí es donde mostrarías los detalles de un producto artesanal específico
    return render_template('product.html', product_id=product_id)

if __name__ == '__main__':
    app.run(debug=True)
