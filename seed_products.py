
import database as dbase
from models.product import Product

def seed_products():
    db = dbase.dbConnection()

    if db is None:
        print("No se pudo conectar con MongoDB.")
        return

    products_col = db["products"]

    products = [
        Product("Leche PIL", "Leche entera de 1 litro", 7.50, 30, "Lácteos y Huevos"),
        Product("Queso fresco", "Queso fresco de 500 gramos", 28.00, 15, "Lácteos y Huevos"),
        Product("Yogur natural", "Yogur natural de 1 litro", 12.00, 20, "Lácteos y Huevos"),
        Product("Pollo entero", "Pollo fresco por unidad", 38.00, 12, "Carnes y Embutidos"),
        Product("Salchichas", "Paquete de salchichas", 18.50, 25, "Carnes y Embutidos"),
        Product("Manzanas", "Manzanas rojas por kilogramo", 12.00, 40, "Frutas y Verduras"),
        Product("Tomates", "Tomates frescos por kilogramo", 8.00, 35, "Frutas y Verduras"),
        Product("Pan de molde", "Pan de molde familiar", 15.00, 18, "Panadería y Pastelería"),
        Product("Galletas", "Paquete de galletas dulces", 6.50, 50, "Panadería y Pastelería"),
        Product("Arroz", "Arroz de primera por kilogramo", 9.00, 45, "Abarrotes y Despensa"),
        Product("Azúcar", "Azúcar blanca por kilogramo", 7.00, 40, "Abarrotes y Despensa"),
        Product("Aceite", "Aceite vegetal de 1 litro", 16.00, 22, "Abarrotes y Despensa"),
        Product("Jugo de naranja", "Jugo de naranja de 1 litro", 11.00, 25, "Bebidas y Jugos"),
        Product("Detergente", "Detergente en polvo de 1 kilogramo", 19.00, 20, "Limpieza y Hogar"),
        Product("Jabón líquido", "Jabón líquido para manos", 14.00, 18, "Cuidado Personal")
    ]

    for product in products:
        data = product.toDBCollection()

        products_col.update_one(
            {"name": data["name"], "category": data["category"]},
            {"$set": data},
            upsert=True
        )

    print("Proceso finalizado. Se prepararon 15 productos.")

if __name__ == "__main__":
    seed_products()
