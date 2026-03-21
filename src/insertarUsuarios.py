
from conexion import coleccion
from usuarios import Usuario


usuario1 = Usuario("Ana Gómez", "ana@gmail.com", 22, ["mongo", "python", "BD"])
usuario2 = Usuario("Carlos López", "carlos@gmail.com", 30, ["programación", "videojuegos"])
usuario3 = Usuario("Laura Martínez", "laura@gmail.com", 27, ["SQL", "python", "mprogramacion"])


usuario_dict = usuario1.to_dict()
resultado = coleccion.insert_one(usuario_dict)
print(f"Usuario insertado con id: {resultado.inserted_id}")


lista_usuarios = [u.to_dict() for u in [usuario2, usuario3]]
resultado_multi = coleccion.insert_many(lista_usuarios)
print(f"Usuarios insertados con ids: {resultado_multi.inserted_ids}")