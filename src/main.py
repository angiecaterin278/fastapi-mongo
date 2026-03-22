from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# 🔌 Conexión a Mongo
client = MongoClient("mongodb+srv://angie28_db:Angie123@cluster0.i2jqedd.mongodb.net/?retryWrites=true&w=majority")

db = client["Angie"]
coleccion = db["Usuarios"]

# ✅ Endpoint mínimo solo para que Render no falle
@app.get("/")
def health_check():
    return {"status": "ok", "mensaje": "Servicio activo (solo consumo interno)"}


# 🔒 FUNCIONES INTERNAS (NO endpoints)

def filtrar_usuarios(nombre: str, edad: int, correo: str):
    filtros = {
        "nombre": nombre,
        "edad": edad,
        "email": correo
    }

    usuarios = []
    for u in coleccion.find(filtros):
        u["_id"] = str(u["_id"])
        usuarios.append(u)

    return usuarios


def crear_usuario(nombre: str, edad: int, correo: str, intereses: str):
    lista_intereses = [i.strip() for i in intereses.split(",")]

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "email": correo,
        "intereses": lista_intereses
    }

    resultado = coleccion.insert_one(usuario)

    return {
        "mensaje": "Usuario creado",
        "id": str(resultado.inserted_id)
    }
