from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()


client = MongoClient("TU_URL_DE_MONGO_ATLAS")
db = client["curso_python"]
coleccion = db["usuarios"]


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando "}


@app.get("/usuarios/{nombre}/{edad}/{correo}")
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
    if usuarios:
        return usuarios
    return {"mensaje": "No se encontraron usuarios con esos datos"}


@app.get("/usuarios/crear/{nombre}/{edad}/{correo}/{intereses}")
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