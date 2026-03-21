from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
    client.server_info()  
    db = client["curso_python"]
    coleccion = db["usuarios"]
    print("Conexión exitosa")
except ConnectionFailure:
    print("Error: No se pudo conectar al servidor MongoDB. Verifica que activo.")
except ConfigurationError:
    print("Error: URI de conexión incorrecta.")
except Exception as e:
    print("Error inesperado:", e)
    