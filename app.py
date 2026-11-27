import os
from flask import Flask, redirect, url_for
from routes.products import products_bp

app = Flask(__name__)
app.secret_key = 'supermercado_secret_key_db2'

# Configuración para subida de imágenes (HU-05)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Registrar rutas modulares
app.register_blueprint(products_bp)

@app.route('/')
def home():
    return redirect(url_for('products.list_products'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)