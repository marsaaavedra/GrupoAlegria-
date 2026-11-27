from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://alejandroreyes_db_user:2026Reyes..@cluster0.i9ajxat.mongodb.net/'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["supermercado_db"]
        return db
    except Exception as e:
        print('Error de conexión con la base de datos:', e)
        return None