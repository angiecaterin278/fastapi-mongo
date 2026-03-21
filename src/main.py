from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# 🔐 Conexión a Mongo Atlas
client = MongoClient("mongodb+srv://angie28_db:Angie123@cluster0.i2jqedd.mongodb.net/?retryWrites=true&w=majority")

# 📦 Base de datos y colección
db = client["Angie"]
coleccion = db["Usuarios"]


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}


@app.get("/usuarios/{nombre}/{edad}/{correo}")
def filtrar_usuarios(nombre: str, edad: int, correo: str):
    try:
        filtros = {
            "nombre": nombre,
            "edad": edad,
            "email": correo
        }

        usuarios = []
        for u in coleccion.find(filtros):
            u["_id"] = str(u["_id"])
            usuarios.append(u)

        if usuarios:
            return usuarios

        return {"mensaje": "No se encontraron usuarios"}

    except Exception as e:
        return {"error": str(e)}


@app.get("/usuarios/crear/{nombre}/{edad}/{correo}/{intereses}")
def crear_usuario(nombre: str, edad: int, correo: str, intereses: str):
    try:
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

    except Exception as e:
        return {"error": str(e)}
