from flask import Blueprint, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
import database as dbase
from models.product import Product, CATEGORIES

products_bp = Blueprint('products', __name__)
db = dbase.dbConnection()

# ==============================================================================
# SECCIÓN INTEGRANTE 1 (HU-04) & INTEGRANTE 4 (HU-10, HU-11): LISTAR Y FILTRAR
# ==============================================================================

@products_bp.route('/products', methods=['GET'])
def list_products():
    products_col = db['products']

    # Obtener parámetros de búsqueda
    name = request.args.get('name', '').strip()
    category = request.args.get('category', '').strip()
    min_price = request.args.get('min_price', '').strip()
    max_price = request.args.get('max_price', '').strip()

    query = {}

    # HU-10: Buscar por nombre
    if name:
        import re
        query['name'] = {
            '$regex': re.escape(name),
            '$options': 'i'
        }

    # HU-10: Filtrar por categoría
    if category:
        if category in CATEGORIES:
            query['category'] = category
        else:
            category = ''

    # HU-11: Filtrar por rango de precio
    price_filter = {}

    try:
        if min_price:
            price_filter['$gte'] = float(min_price)

        if max_price:
            price_filter['$lte'] = float(max_price)

        if any(value < 0 for value in price_filter.values()):
            raise ValueError

        if min_price and max_price and float(min_price) > float(max_price):
            flash('El precio mínimo no puede superar al máximo.', 'warning')
            price_filter = {}

    except ValueError:
        flash('Ingresa precios válidos y positivos.', 'warning')
        price_filter = {}

    if price_filter:
        query['price'] = price_filter

    # Consultar productos con todos los filtros
    products_list = list(products_col.find(query).sort('name', 1))

    return render_template(
        'index.html',
        products=products_list,
        categories=CATEGORIES,
        name=name,
        category=category,
        min_price=min_price,
        max_price=max_price
    )


# ==============================================================================
# SECCIÓN INTEGRANTE 2 (HU-03, HU-05, HU-08): CREAR PRODUCTO E IMÁGENES
# ==============================================================================
@products_bp.route('/products/new', methods=['GET', 'POST'])
def create_product():
    # TODO: Integrante 2 implementa el formulario GET y el guardado POST aquí
    flash("Vista /products/new en construcción (Integrante 2)", "info")
    return redirect(url_for('products.list_products'))


# ==============================================================================
# SECCIÓN INTEGRANTE 3 (HU-06): VER DETALLE DEL PRODUCTO
# ==============================================================================
@products_bp.route('/products/<id>', methods=['GET'])
def detail_product(id):
    # TODO: Integrante 3 implementa la consulta por ObjectId(id) y detail.html
    flash("Vista /products/<id> en construcción (Integrante 3)", "info")
    return redirect(url_for('products.list_products'))


# ==============================================================================
# SECCIÓN INTEGRANTE 3 (HU-07): EDITAR PRODUCTO
# ==============================================================================
@products_bp.route('/products/<id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    # TODO: Integrante 3 implementa la carga de datos y update_one aquí
    flash("Vista /products/<id>/edit en construcción (Integrante 3)", "info")
    return redirect(url_for('products.list_products'))


# ==============================================================================
# SECCIÓN INTEGRANTE 3 (HU-09): ELIMINAR PRODUCTO (CONFIRMACIÓN)
# ==============================================================================
@products_bp.route('/products/<id>/delete', methods=['GET', 'POST'])
def delete_product(id):
    # TODO: Integrante 3 implementa pantalla de confirmación GET y delete_one POST
    flash("Vista /products/<id>/delete en construcción (Integrante 3)", "info")
    return redirect(url_for('products.list_products'))