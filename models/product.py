CATEGORIES = [
    "Lácteos y Huevos",
    "Carnes y Embutidos",
    "Frutas y Verduras",
    "Panadería y Pastelería",
    "Abarrotes y Despensa",
    "Bebidas y Jugos",
    "Limpieza y Hogar",
    "Cuidado Personal"
]

class Product:
    def __init__(self, name, description, price, stock, category, image=""):
        self.name = name
        self.description = description
        self.price = float(price)
        self.stock = int(stock)
        self.category = category
        self.image = image if image else "/static/img/default-product.png"

    def toDBCollection(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category': self.category,
            'image': self.image
        }